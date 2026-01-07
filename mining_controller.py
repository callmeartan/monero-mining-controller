import os
import json
import time
import subprocess
import threading
import signal
import sys
from pathlib import Path
import psutil
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.columns import Columns
from rich.align import Align
from rich.markdown import Markdown

class PoolSelector:
    """Handles pool selection and comparison"""

    def __init__(self, pools_file="pools.json"):
        self.pools_file = pools_file
        self.pools = []
        self.load_pools()

    def load_pools(self):
        """Load pool data from JSON file"""
        try:
            with open(self.pools_file, 'r') as f:
                data = json.load(f)
                self.pools = data.get('pools', [])
                self.notes = data.get('notes', {})
        except FileNotFoundError:
            print(f"Pools file {self.pools_file} not found!")
            self.pools = []
            self.notes = {}
        except json.JSONDecodeError:
            print(f"Invalid pools file {self.pools_file}!")
            self.pools = []
            self.notes = {}

    def display_pool_comparison(self, console):
        """Display comparison table of available pools"""
        if not self.pools:
            console.print("[red]No pools available![/red]")
            return

        table = Table(title="Monero Mining Pool Comparison")
        table.add_column("Pool Name", style="cyan", no_wrap=True)
        table.add_column("Fee %", style="yellow", justify="right")
        table.add_column("Min Payout", style="green", justify="right")
        table.add_column("Type", style="magenta")
        table.add_column("Location", style="blue")
        table.add_column("Description", style="white")

        for pool in self.pools:
            fee = f"{pool['fee']:.1f}"
            min_payout = f"{pool['min_payout']:.4f}"
            recommended_marker = " ⭐" if pool.get('recommended', False) else ""

            table.add_row(
                pool['name'] + recommended_marker,
                fee,
                min_payout,
                pool['type'],
                pool['location'],
                pool['description']
            )

        console.print(table)

        # Show recommendations
        if 'recommendations' in self.notes:
            console.print("\n[bold]Recommendations:[/bold]")
            recs = self.notes['recommendations']
            for category, recommendation in recs.items():
                console.print(f"• [cyan]{category.title()}[/cyan]: {recommendation}")

    def select_pool_interactive(self, console):
        """Interactive pool selection"""
        self.display_pool_comparison(console)

        console.print("\n[bold]Pool Selection Options:[/bold]")
        for i, pool in enumerate(self.pools, 1):
            recommended = " ⭐" if pool.get('recommended', False) else ""
            console.print(f"{i}. {pool['name']}{recommended}")

        console.print(f"{len(self.pools) + 1}. Enter custom pool details")

        while True:
            try:
                choice = IntPrompt.ask(
                    f"\nSelect a pool (1-{len(self.pools) + 1})",
                    default=1
                )

                if 1 <= choice <= len(self.pools):
                    selected_pool = self.pools[choice - 1]
                    console.print(f"[green]Selected: {selected_pool['name']}[/green]")
                    return selected_pool
                elif choice == len(self.pools) + 1:
                    return self.add_custom_pool(console)
                else:
                    console.print("[red]Invalid choice![/red]")

            except KeyboardInterrupt:
                return None

    def add_custom_pool(self, console):
        """Add a custom pool"""
        console.print("[bold]Add Custom Pool[/bold]")

        name = Prompt.ask("Pool name")
        url = Prompt.ask("Pool URL (without port)")
        port = IntPrompt.ask("Pool port")
        fee = float(Prompt.ask("Pool fee (%)", default="1.0"))
        min_payout = float(Prompt.ask("Minimum payout (XMR)", default="0.1"))

        custom_pool = {
            "name": name,
            "url": url,
            "port": port,
            "fee": fee,
            "min_payout": min_payout,
            "type": "Custom",
            "location": "Custom",
            "description": f"Custom pool: {name}",
            "features": ["Custom configuration"],
            "recommended": False
        }

        console.print(f"[green]Added custom pool: {name}[/green]")
        return custom_pool

    def get_pool_info(self, pool_name):
        """Get pool information by name"""
        for pool in self.pools:
            if pool['name'].lower() == pool_name.lower():
                return pool
        return None

class CPUController:
    """Handles CPU configuration and control"""

    def __init__(self, config_file="config.json"):
        self.config_file = config_file

    def get_cpu_info(self):
        """Get CPU information"""
        return {
            'physical_cores': psutil.cpu_count(logical=False),
            'logical_cores': psutil.cpu_count(logical=True),
            'usage_percent': psutil.cpu_percent(interval=1)
        }

    def update_cpu_config(self, max_threads=None, priority=None, affinity=None):
        """Update CPU configuration in XMRig config"""
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return False

        if 'cpu' not in config:
            config['cpu'] = {}

        updated = False

        if max_threads is not None:
            # Set CPU affinity to use specific cores
            if max_threads > 0:
                cores_to_use = min(max_threads, psutil.cpu_count(logical=True))
                affinity_str = ",".join(str(i) for i in range(cores_to_use))
                config['cpu']['affinity'] = affinity_str
                updated = True

        if priority is not None:
            # Set CPU priority (0=highest to 5=lowest)
            if 0 <= priority <= 5:
                config['cpu']['priority'] = priority
                updated = True

        if affinity is not None:
            config['cpu']['affinity'] = affinity
            updated = True

        if updated:
            try:
                with open(self.config_file, 'w') as f:
                    json.dump(config, f, indent=4)
                return True
            except Exception:
                return False

        return False

    def get_current_config(self):
        """Get current CPU configuration"""
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                return config.get('cpu', {})
        except:
            return {}

    def display_cpu_config(self, console):
        """Display current CPU configuration"""
        cpu_info = self.get_cpu_info()
        current_config = self.get_current_config()

        table = Table(title="CPU Configuration")
        table.add_column("Setting", style="cyan")
        table.add_column("Current Value", style="green")
        table.add_column("Description", style="white")

        table.add_row("Physical Cores", str(cpu_info['physical_cores']), "Physical CPU cores")
        table.add_row("Logical Cores", str(cpu_info['logical_cores']), "Logical CPU cores (including hyperthreading)")
        table.add_row("Current Usage", f"{cpu_info['usage_percent']:.1f}%", "Current CPU usage")

        affinity = current_config.get('affinity', 'Auto')
        if isinstance(affinity, str) and affinity != 'Auto':
            affinity_cores = len(affinity.split(','))
            table.add_row("Active Threads", str(affinity_cores), "Number of CPU threads allocated to mining")
        else:
            table.add_row("Active Threads", "Auto", "Automatic thread allocation")

        priority = current_config.get('priority')
        if priority is not None:
            priority_desc = {
                0: "Highest (most aggressive)",
                1: "High",
                2: "Above normal",
                3: "Normal",
                4: "Below normal",
                5: "Lowest (most conservative)"
            }.get(priority, f"Level {priority}")
            table.add_row("CPU Priority", f"{priority} ({priority_desc})", "Mining process priority")
        else:
            table.add_row("CPU Priority", "Default", "System default priority")

        console.print(table)

class MiningMonitor:
    """Handles XMRig process monitoring and statistics parsing"""

    def __init__(self, xmrig_process=None):
        self.xmrig_process = xmrig_process
        self.stats = {
            'hashrate': 0.0,
            'shares': {'accepted': 0, 'rejected': 0},
            'uptime': 0,
            'start_time': time.time()
        }
        self.monitoring = False
        self.monitor_thread = None

    def start_monitoring(self, xmrig_process):
        """Start monitoring XMRig process"""
        self.xmrig_process = xmrig_process
        self.monitoring = True
        self.start_time = time.time()
        self.monitor_thread = threading.Thread(target=self._monitor_output)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

    def stop_monitoring(self):
        """Stop monitoring"""
        self.monitoring = False
        if self.monitor_thread and self.monitor_thread.is_alive():
            self.monitor_thread.join(timeout=2)

    def _monitor_output(self):
        """Monitor XMRig stdout for statistics"""
        if not self.xmrig_process:
            return

        try:
            while self.monitoring and self.xmrig_process.poll() is None:
                # Read stdout line by line
                if hasattr(self.xmrig_process, 'stdout') and self.xmrig_process.stdout:
                    line = self.xmrig_process.stdout.readline()
                    if line:
                        self._parse_xmrig_line(line.decode('utf-8', errors='ignore').strip())
                time.sleep(0.1)
        except Exception:
            pass  # Silently handle monitoring errors

    def _parse_xmrig_line(self, line):
        """Parse XMRig output line for statistics"""
        line = line.lower()

        # Parse hashrate (various formats)
        if any(keyword in line for keyword in ['speed', 'h/s', 'hashrate']):
            try:
                # Look for patterns like "speed 2.5s/60s/15m H/s max"
                if 'h/s' in line:
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if 'h/s' in part:
                            # Get the value before h/s
                            rate_part = parts[i-1] if i > 0 else ""
                            if rate_part:
                                # Handle K, M, G suffixes
                                multiplier = 1
                                if rate_part.endswith('k'):
                                    multiplier = 1000
                                    rate_part = rate_part[:-1]
                                elif rate_part.endswith('m'):
                                    multiplier = 1000000
                                    rate_part = rate_part[:-1]
                                elif rate_part.endswith('g'):
                                    multiplier = 1000000000
                                    rate_part = rate_part[:-1]

                                try:
                                    self.stats['hashrate'] = float(rate_part) * multiplier
                                except ValueError:
                                    pass
                            break
            except:
                pass

        # Parse accepted shares
        if 'accepted' in line and ('share' in line or 'shares' in line):
            try:
                # Look for patterns like "accepted (123/0) diff"
                import re
                match = re.search(r'accepted\s*\((\d+)/(\d+)\)', line)
                if match:
                    accepted = int(match.group(1))
                    rejected = int(match.group(2))
                    self.stats['shares']['accepted'] = accepted
                    self.stats['shares']['rejected'] = rejected
            except:
                pass

    def get_system_stats(self):
        """Get current system statistics"""
        return {
            'cpu_usage': psutil.cpu_percent(interval=0.1),
            'memory': psutil.virtual_memory().percent,
            'cpu_cores': psutil.cpu_count(logical=True),
            'uptime': time.time() - self.start_time
        }

    def is_xmrig_running(self):
        """Check if XMRig process is still running"""
        if not self.xmrig_process:
            return False
        return self.xmrig_process.poll() is None

    def get_stats_summary(self):
        """Get formatted statistics summary"""
        system_stats = self.get_system_stats()
        uptime_str = self._format_uptime(system_stats['uptime'])

        return {
            'hashrate': self.stats['hashrate'],
            'accepted_shares': self.stats['shares']['accepted'],
            'rejected_shares': self.stats['shares']['rejected'],
            'cpu_usage': system_stats['cpu_usage'],
            'memory_usage': system_stats['memory'],
            'uptime': uptime_str,
            'cpu_cores': system_stats['cpu_cores'],
            'status': 'Running' if self.is_xmrig_running() else 'Stopped'
        }

    def _format_uptime(self, seconds):
        """Format uptime in human readable format"""
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds = divmod(remainder, 60)

        if hours > 0:
            return f"{hours}h {minutes}m {seconds}s"
        elif minutes > 0:
            return f"{minutes}m {seconds}s"
        else:
            return f"{seconds}s"

class XMRigController:
    """Main controller for XMRig process management"""

    def __init__(self, xmrig_path="./xmrig", config_path="./config.json"):
        self.xmrig_path = xmrig_path
        self.config_path = config_path
        self.xmrig_process = None
        self.monitor = MiningMonitor()

    def load_config(self):
        """Load XMRig configuration"""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Config file not found: {self.config_path}")
            return None
        except json.JSONDecodeError:
            print(f"Invalid config file: {self.config_path}")
            return None

    def save_config(self, config):
        """Save XMRig configuration"""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False

    def update_pool_config(self, pool_info, wallet_address):
        """Update pool configuration in XMRig config"""
        config = self.load_config()
        if not config:
            return False

        if 'pools' not in config or not config['pools']:
            config['pools'] = [{}]

        pool_config = config['pools'][0]
        pool_config.update({
            'coin': 'monero',
            'url': f"{pool_info['url']}:{pool_info['port']}",
            'user': wallet_address,
            'pass': 'x',
            'tls': True,
            'keepalive': True,
            'nicehash': False
        })

        return self.save_config(config)

    def start_mining(self):
        """Start XMRig mining process"""
        if self.monitor.is_xmrig_running():
            return False, "XMRig is already running"

        try:
            self.xmrig_process = subprocess.Popen(
                [self.xmrig_path, "-c", self.config_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )

            self.monitor.start_monitoring(self.xmrig_process)
            return True, "XMRig started successfully"
        except Exception as e:
            return False, f"Failed to start XMRig: {e}"

    def stop_mining(self):
        """Stop XMRig mining process"""
        if not self.monitor.is_xmrig_running():
            return False, "XMRig is not running"

        try:
            if self.xmrig_process:
                self.xmrig_process.terminate()
                self.xmrig_process.wait(timeout=5)
            self.monitor.stop_monitoring()
            return True, "XMRig stopped"
        except subprocess.TimeoutExpired:
            self.xmrig_process.kill()
            self.monitor.stop_monitoring()
            return True, "XMRig force killed"
        except Exception as e:
            return False, f"Error stopping XMRig: {e}"

    def restart_mining(self):
        """Restart XMRig with new configuration"""
        success, message = self.stop_mining()
        if not success:
            return False, message

        time.sleep(1)  # Brief pause
        return self.start_mining()

class MiningUI:
    """Main terminal user interface"""

    def __init__(self):
        self.console = Console()
        self.pool_selector = PoolSelector()
        self.cpu_controller = CPUController()
        self.xmrig_controller = XMRigController()
        self.monitor = self.xmrig_controller.monitor
        self.running = True
        self.selected_pool = None
        self.wallet_address = None

    def create_stats_panel(self):
        """Create statistics display panel"""
        stats = self.monitor.get_stats_summary()

        table = Table(title="Mining Statistics")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Status", stats['status'])
        table.add_row("Hashrate", f"{stats['hashrate']:.1f} H/s" if stats['hashrate'] > 0 else "N/A")
        table.add_row("Accepted Shares", str(stats['accepted_shares']))
        table.add_row("Rejected Shares", str(stats['rejected_shares']))
        table.add_row("CPU Usage", f"{stats['cpu_usage']:.1f}%")
        table.add_row("Memory Usage", f"{stats['memory_usage']:.1f}%")
        table.add_row("Uptime", stats['uptime'])

        return Panel(table, title="Statistics", border_style="blue")

    def create_menu_panel(self):
        """Create control menu panel"""
        menu_text = Text()
        menu_text.append("Control Menu:\n\n", style="bold blue")

        if not self.selected_pool:
            menu_text.append("1. Select Mining Pool\n", style="yellow")
        else:
            menu_text.append(f"1. Change Mining Pool (Current: {self.selected_pool['name']})\n", style="green")

        if not self.wallet_address:
            menu_text.append("2. Set Wallet Address\n", style="yellow")
        else:
            menu_text.append("2. Change Wallet Address\n", style="green")

        menu_text.append("3. Configure CPU Usage\n", style="cyan")
        menu_text.append("4. Start Mining\n", style="green")
        menu_text.append("5. Stop Mining\n", style="red")
        menu_text.append("6. Restart with New Settings\n", style="magenta")
        menu_text.append("7. View Current Configuration\n", style="white")
        menu_text.append("8. View Pool Comparison\n", style="white")
        menu_text.append("0. Exit\n", style="red")

        return Panel(menu_text, title="Menu", border_style="green")

    def handle_menu_choice(self, choice):
        """Handle menu selection"""
        if choice == "1":
            self.selected_pool = self.pool_selector.select_pool_interactive(self.console)
            if self.selected_pool:
                self.console.print(f"[green]Pool selected: {self.selected_pool['name']}[/green]")

        elif choice == "2":
            self._set_wallet_address()

        elif choice == "3":
            self._configure_cpu()

        elif choice == "4":
            if not self.selected_pool:
                self.console.print("[red]Please select a mining pool first![/red]")
                return
            if not self.wallet_address:
                self.console.print("[red]Please set your wallet address first![/red]")
                return

            # Update config with pool and wallet
            if self.xmrig_controller.update_pool_config(self.selected_pool, self.wallet_address):
                success, message = self.xmrig_controller.start_mining()
                if success:
                    self.console.print(f"[green]{message}[/green]")
                else:
                    self.console.print(f"[red]{message}[/red]")
            else:
                self.console.print("[red]Failed to update configuration[/red]")

        elif choice == "5":
            success, message = self.xmrig_controller.stop_mining()
            if success:
                self.console.print(f"[yellow]{message}[/yellow]")
            else:
                self.console.print(f"[red]{message}[/red]")

        elif choice == "6":
            if not self.selected_pool or not self.wallet_address:
                self.console.print("[red]Please select pool and set wallet address first![/red]")
                return

            if self.xmrig_controller.update_pool_config(self.selected_pool, self.wallet_address):
                success, message = self.xmrig_controller.restart_mining()
                if success:
                    self.console.print(f"[green]{message}[/green]")
                else:
                    self.console.print(f"[red]{message}[/red]")
            else:
                self.console.print("[red]Failed to update configuration[/red]")

        elif choice == "7":
            self._view_configuration()

        elif choice == "8":
            self.pool_selector.display_pool_comparison(self.console)

        elif choice == "0":
            self.xmrig_controller.stop_mining()
            self.running = False

        else:
            self.console.print("[red]Invalid choice![/red]")

    def _set_wallet_address(self):
        """Set wallet address"""
        while True:
            wallet = Prompt.ask("Enter your Monero wallet address")
            if wallet and len(wallet) > 50:  # Basic validation
                self.wallet_address = wallet
                self.console.print("[green]Wallet address set![/green]")
                break
            else:
                self.console.print("[red]Invalid wallet address. Please try again.[/red]")

    def _configure_cpu(self):
        """Configure CPU usage"""
        cpu_info = self.cpu_controller.get_cpu_info()
        max_cores = cpu_info['logical_cores']

        self.cpu_controller.display_cpu_config(self.console)

        self.console.print(f"\n[bold]CPU Configuration:[/bold]")
        self.console.print(f"Available cores: {max_cores}")

        # Configure threads
        threads = IntPrompt.ask(
            f"Number of CPU threads to use (1-{max_cores})",
            default=min(4, max_cores)
        )

        if 1 <= threads <= max_cores:
            # Configure priority
            priority = IntPrompt.ask(
                "CPU priority (0=highest, 5=lowest)",
                default=3
            )

            if 0 <= priority <= 5:
                if self.cpu_controller.update_cpu_config(max_threads=threads, priority=priority):
                    self.console.print(f"[green]CPU configured: {threads} threads, priority {priority}[/green]")
                else:
                    self.console.print("[red]Failed to update CPU configuration[/red]")
            else:
                self.console.print("[red]Invalid priority level[/red]")
        else:
            self.console.print("[red]Invalid thread count[/red]")

    def _view_configuration(self):
        """View current configuration"""
        config = self.xmrig_controller.load_config()
        if config:
            self.console.print("[bold]Current Configuration:[/bold]")
            self.console.print_json(json.dumps(config, indent=2))
        else:
            self.console.print("[red]Could not load configuration[/red]")

    def run(self):
        """Main UI loop"""
        self.console.clear()
        self.console.print("[bold blue]🚀 Monero Mining Controller[/bold blue]")
        self.console.print("[dim]Control your XMRig mining with dynamic CPU allocation[/dim]\n")

        # Setup signal handlers
        def signal_handler(sig, frame):
            self.console.print("\n[yellow]Shutting down...[/yellow]")
            self.xmrig_controller.stop_mining()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

        with Live(console=self.console, refresh_per_second=2) as live:
            while self.running:
                # Create layout
                stats_panel = self.create_stats_panel()
                menu_panel = self.create_menu_panel()

                layout = Columns([stats_panel, menu_panel], equal=True)
                live.update(Align.center(layout))

                # Get user input
                try:
                    choice = Prompt.ask("", console=self.console, show_default=False)
                    self.handle_menu_choice(choice)
                except KeyboardInterrupt:
                    self.xmrig_controller.stop_mining()
                    break
                except EOFError:
                    break

        self.console.print("[yellow]Goodbye![/yellow]")

def main():
    """Main application entry point"""
    # Check if running on macOS
    if sys.platform != "darwin":
        print("This application is designed for macOS")
        sys.exit(1)

    # Check for required files
    required_files = ["./xmrig", "./config.json", "./pools.json"]
    missing_files = []

    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)

    if missing_files:
        print("Missing required files:")
        for file in missing_files:
            print(f"  - {file}")
        print("\nPlease ensure all required files are present before running.")
        sys.exit(1)

    # Check Python dependencies
    try:
        import rich
        import psutil
    except ImportError as e:
        print(f"Missing Python dependencies: {e}")
        print("Please install required packages:")
        print("  pip install rich psutil")
        sys.exit(1)

    # Start the UI
    ui = MiningUI()
    ui.run()

if __name__ == "__main__":
    main()

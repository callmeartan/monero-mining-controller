# 🚀 Monero Mining Controller

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-blue)](https://github.com/xmrig/xmrig)

> A professional, feature-rich terminal application for controlling XMRig Monero mining operations with intelligent CPU management, real-time monitoring, and performance analytics.

## 📋 Table of Contents

- [✨ Key Features](#-key-features)
- [📋 Requirements](#-requirements)
- [🚀 Installation](#-installation)
- [⚡ Quick Start](#-quick-start)
- [📖 User Guide](#-user-guide)
- [⚙️ Configuration](#️-configuration)
- [🔧 Troubleshooting](#-troubleshooting)
- [📊 Performance Optimization](#-performance-optimization)
- [🔒 Security & Privacy](#-security--privacy)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## ✨ Key Features

### 🎯 Mining Management
- **Interactive Pool Selection** - Compare 6+ popular pools with detailed metrics
- **Dynamic CPU Control** - Real-time thread and priority adjustment
- **Process Management** - Start, stop, restart with configuration updates
- **Settings Persistence** - Remembers your pool and wallet between sessions

### 📊 Advanced Monitoring
- **Real-Time Dashboard** - Live statistics with auto-refresh
- **Performance Analytics** - Peak hashrate tracking and acceptance rates
- **Visual Feedback** - Dynamic emojis and colors based on mining performance:
  - 🐌 **Slow** (< 1 KH/s)
  - 👍 **Good** (1-10 KH/s)
  - 🚀 **Fast** (10-100 KH/s)
  - 🔥 **Blazing** (100 KH/s - 1 MH/s)
  - ⚡💎 **Legendary** (≥ 1 MH/s)
- **System Monitoring** - Color-coded CPU/memory usage indicators

### 🛠️ Developer Experience
- **Cross-Platform** - Native support for macOS, Linux, and Windows
- **Automated Setup** - One-command installation with dependency management
- **Comprehensive Logging** - XMRig log viewing and troubleshooting tools
- **Configuration Validation** - Input validation and error handling
- **Keyboard Navigation** - Intuitive menu-driven interface

## 📋 Requirements

### System Requirements
- **Operating System**:
  - macOS 10.15+ (Intel/Apple Silicon)
  - Linux (x86_64, ARM64)
  - Windows 10+ (x64)
- **Python**: 3.8 or higher
- **RAM**: 512MB minimum, 1GB recommended
- **Storage**: 50MB free space
- **Network**: Stable internet connection

### Mining Requirements
- **Monero Wallet**: Valid XMR address (starts with `4` or `8`)
- **Mining Pool**: Active Monero mining pool
- **Hardware**: Any modern CPU (mining performance varies by core count/speed)

### Dependencies
- `rich` - Terminal UI framework
- `psutil` - System monitoring
- `XMRig` - Mining software (auto-downloaded)

## 🚀 Installation

### Automated Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/monero-mining-controller.git
cd monero-mining-controller

# Run automated setup
python setup.py
```

**What the setup does:**
- ✅ Validates Python version and system compatibility
- ✅ Installs required Python packages (`rich`, `psutil`)
- ✅ Downloads appropriate XMRig binary for your platform
- ✅ Creates initial configuration files
- ✅ Sets up proper file permissions

### Manual Installation

```bash
# Install Python dependencies
pip install rich psutil

# Download XMRig manually from https://github.com/xmrig/xmrig/releases
# Place the xmrig executable in the project directory

# Create basic configuration
cp config.json.example config.json
```

### Verification

```bash
# Test installation
python -c "import rich, psutil; print('✅ Dependencies installed')"
ls -la xmrig*  # Check for XMRig binary
```

## ⚡ Quick Start

### First-Time Setup (5 minutes)

```bash
# 1. Launch the application
python mining_controller.py

# 2. Follow the interactive setup:
#    - Press 1: Select mining pool (MoneroOcean recommended)
#    - Press 2: Enter your Monero wallet address
#    - Press 3: Configure CPU threads (start with 50% of cores)
#    - Press 4: Start mining!
```

### Subsequent Runs (10 seconds)

   ```bash
   python mining_controller.py
# Press 4 to start mining immediately (settings remembered)
```

### Example Session

```
🚀 Monero Mining Controller

✅ Ready to mine! Pool: MoneroOcean | Wallet: 4ABC...
Press 4 to start mining immediately

[Statistics Panel]          [Menu]
┌─ Mining Statistics ─┐    ┌─ Control Menu ─┐
│ Status: ▶️ Running   │    │ 4. Start Mining│
│ Hashrate: 2.4 KH/s 🚀│    │ 5. Stop Mining│
│ Peak: 3.1 KH/s      │    │ 0. Exit        │
└─────────────────────┘    └────────────────┘

Mining started successfully!
```

## 📖 User Guide

### Interface Overview

The application uses a dual-panel terminal interface:

```
┌─ Mining Statistics ──────────┐    ┌─ Control Menu ──────────────────┐
│ Status: ▶️ Running            │    │ 1. Change Mining Pool           │
│ Hashrate: 2.4 KH/s 🚀         │    │    (Current: MoneroOcean)       │
│ Peak Hashrate: 3.1 KH/s       │    │ 2. Change Wallet Address        │
│ Accepted Shares: 45          │    │ 4. Start Mining                 │
│ Rejected Shares: 2           │    │ 5. Stop Mining                  │
│ Acceptance Rate: 95.7%       │    │ 0. Exit Application             │
│ CPU Usage: 75.2%             │    │                                 │
│ Memory Usage: 68.1%          │    │                                 │
│ Uptime: 1h 23m 45s          │    └─────────────────────────────────┘
└──────────────────────────────┘
```

### Menu Options

| Option | Description | When to Use |
|--------|-------------|-------------|
| **1** | Select/Change Mining Pool | Initial setup or switching pools |
| **2** | Set/Change Wallet Address | Initial setup or wallet change |
| **3** | Configure CPU Usage | Optimize mining performance |
| **4** | Start Mining | Begin mining with current config |
| **5** | Stop Mining | Pause mining operations |
| **6** | Restart Mining | Apply configuration changes |
| **7** | View Configuration | Check current XMRig settings |
| **8** | View Pool Comparison | Compare available pools |
| **9** | View XMRig Logs | Debug connection/mining issues |
| **10** | Check Mining Status | Diagnose mining process health |
| **11** | Troubleshoot Connection | Fix pool connectivity issues |
| **12** | Reset Settings | Clear saved preferences |
| **0** | Exit Application | Close the mining controller |

### Mining Pool Selection

#### Recommended Pools

| Pool | Fee | Min Payout | Payout Freq | Best For |
|------|-----|------------|-------------|----------|
| **MoneroOcean** ⭐⭐⭐ | 0.5% | 0.003 XMR | Hourly | Most users, frequent payouts |
| **SupportXMR** ⭐⭐ | 0.6% | 0.1 XMR | Daily | Beginners, community support |
| **MineXMR** ⭐⭐ | 1.0% | 0.1 XMR | Daily | Stable, established pool |
| **P2Pool** ⭐⭐ | 0% | 0.0003 XMR | 30min | Privacy-focused, decentralized |
| **Nanopool** | 1.0% | 1.0 XMR | Daily | Large-scale operations |
| **HashVault** | 0.9% | 0.5 XMR | Daily | Good performance balance |

#### Pool Selection Tips

- **For Beginners**: Start with **MoneroOcean** - low fees, frequent payouts, easy setup
- **For Privacy**: Use **P2Pool** - decentralized, no central operator
- **For Reliability**: Choose pools with multiple server locations
- **For Large Operations**: Consider pools with lower minimum payouts

#### Custom Pool Configuration

1. Select option 1 → Choose "Enter custom pool details"
2. Enter pool URL (without port)
3. Specify port number
4. Set pool fee percentage
5. Configure minimum payout threshold

### Wallet Configuration

#### Supported Address Formats

- **Standard Address**: Starts with `4` (95 characters)
- **Integrated Address**: Starts with `4` (106 characters)
- **Subaddress**: Starts with `8` (95 characters)

#### Security Recommendations

- ✅ Use a dedicated mining wallet
- ✅ Enable 2FA on your wallet if available
- ✅ Never reuse addresses for different purposes
- ❌ Avoid using exchange deposit addresses for mining

### CPU Configuration

#### Optimal Thread Count

| CPU Cores | Recommended Threads | Performance Notes |
|-----------|-------------------|-------------------|
| 2-4 | 1-2 | Basic mining, low power usage |
| 6-8 | 3-4 | Balanced performance |
| 10-16 | 5-8 | High performance mining |
| 16+ | 8-12 | Maximum mining throughput |

#### CPU Priority Levels

| Priority | Level | Description | Use Case |
|----------|-------|-------------|----------|
| 0 | Highest | Maximum mining priority | Dedicated mining rigs |
| 1 | High | Very high priority | Primary mining machines |
| 2 | Above Normal | High priority | Secondary mining |
| 3 | Normal | Standard priority | General use machines |
| 4 | Below Normal | Low priority | Background mining |
| 5 | Lowest | Minimum priority | Non-critical systems |

#### Performance Tuning

1. **Start Conservative**: Begin with 50% of available cores
2. **Monitor Temperatures**: Ensure CPU stays under 80°C
3. **Test Gradually**: Increase threads incrementally
4. **Balance Usage**: Leave 1-2 cores free for system responsiveness

### Real-Time Monitoring

The dashboard provides comprehensive mining analytics with visual performance indicators:

#### Performance Metrics

| Metric | Description | Visual Indicators |
|--------|-------------|-------------------|
| **Mining Status** | Current mining state | ▶️ Running, ⏹️ Stopped, ⏳ Starting |
| **Hashrate** | Current mining speed | Color-coded with performance emojis |
| **Peak Hashrate** | Best performance achieved | Historical tracking |
| **Accepted Shares** | Successfully submitted shares | Green counter |
| **Rejected Shares** | Failed share submissions | Red counter |
| **Acceptance Rate** | Share acceptance percentage | Color-coded percentage |
| **CPU Usage** | Processor utilization | Green (<70%), Yellow (70-90%), Red (>90%) |
| **Memory Usage** | RAM utilization | Green (<70%), Yellow (70-90%), Red (>90%) |
| **Uptime** | Mining session duration | HH:MM:SS format |

#### Performance Tiers

| Tier | Hashrate Range | Visual Style | Description |
|------|----------------|--------------|-------------|
| **🐌 Slow** | < 1 KH/s | Yellow text | Starting/initial phase |
| **👍 Good** | 1-10 KH/s | Green text | Decent performance |
| **🚀 Fast** | 10-100 KH/s | Bright green + rocket | Excellent performance |
| **🔥 Blazing** | 100 KH/s - 1 MH/s | Bold green + fire | High-performance mining |
| **⚡💎 Legendary** | ≥ 1 MH/s | Cyan + lightning + diamond | Exceptional performance |

#### System Health Indicators

- **🟢 Green**: Optimal performance range
- **🟡 Yellow**: Elevated usage, monitor closely
- **🔴 Red**: High usage, consider reducing load

## ⚙️ Configuration

### Configuration Files

| File | Purpose | Auto-Generated | Editable |
|------|---------|----------------|----------|
| `config.json` | XMRig mining configuration | ✅ | ✅ |
| `pools.json` | Mining pool database | ❌ | ✅ |
| `user_settings.json` | User preferences | ✅ | ❌ |
| `xmrig.log` | Mining operation logs | ✅ | ❌ |
| `requirements.txt` | Python dependencies | ❌ | ❌ |

### XMRig Configuration Options

#### Core Settings

```json
{
  "autosave": true,
  "background": false,
  "colors": true,
  "cpu": {
    "enabled": true,
    "huge-pages": true,
    "priority": 3,
    "max-threads-hint": 100
  },
  "pools": [
    {
      "url": "gulf.moneroocean.stream:10001",
      "user": "YOUR_WALLET_ADDRESS",
      "pass": "x",
      "tls": false,
      "keepalive": true
    }
  ]
}
```

#### Advanced Options

| Setting | Description | Recommended Value |
|---------|-------------|-------------------|
| `huge-pages` | Memory optimization | `true` |
| `priority` | CPU scheduling priority | `3` (Normal) |
| `max-threads-hint` | Maximum mining threads | `100` |
| `keepalive` | Maintain pool connection | `true` |
| `tls` | Use SSL encryption | `false` (for compatibility) |

### User Preferences

The application automatically saves your settings:

```json
{
  "selected_pool": {
    "name": "MoneroOcean",
    "url": "gulf.moneroocean.stream",
    "port": 10001,
    "fee": 0.5
  },
  "wallet_address": "4ABC...your_wallet_address"
}
```

### Logging Configuration

XMRig logging is automatically configured:

```json
{
  "log-file": "xmrig.log",
  "verbose": 1,
  "syslog": false,
  "print-time": 60
}
```

## 🔧 Troubleshooting

### Common Issues & Solutions

#### ❌ "Connection Failed" / "End of File" Errors

**Symptoms:**
```
[2026-01-07 04:59:54.571] net gulf.moneroocean.stream:10128 read error: "end of file"
```

**Solutions:**
1. **Disable TLS**: Many pools work better without SSL
   - Use option 11 → Press 1 to disable TLS
2. **Switch Ports**: Try alternative ports (10001, 10002, 10128)
   - Use option 11 → Press 2 to change port
3. **Try Different Server**: Use backup pool servers
   - Use option 11 → Press 3 to switch servers
4. **Check Network**: Ensure stable internet connection

#### ❌ "XMRig Failed to Start"

**Possible Causes:**
- Missing XMRig binary
- Incorrect file permissions
- Configuration errors
- Port conflicts

**Solutions:**
```bash
# Check XMRig exists and is executable
ls -la xmrig*

# Make executable (macOS/Linux)
chmod +x xmrig

# Check configuration
python mining_controller.py
# Press 7 to view current config
```

#### ❌ Low Hashrate

**Common Causes:**
- Insufficient CPU threads
- High CPU priority causing throttling
- Background applications consuming resources
- Thermal throttling

**Optimization Steps:**
1. Increase thread count (option 3)
2. Lower CPU priority (0-2 for better performance)
3. Close unnecessary applications
4. Monitor CPU temperature (<80°C recommended)

#### ❌ High CPU/Memory Usage

**System Impact:**
- Mining uses significant system resources
- Normal behavior for CPU mining
- Monitor for thermal issues

**Management:**
- Reduce thread count if system becomes unresponsive
- Use lower CPU priority for background mining
- Consider dedicated mining hardware

### Diagnostic Tools

#### Built-in Diagnostics

```bash
python mining_controller.py
# Press 10: Check Mining Status
# Press 11: Troubleshoot Connection
# Press 9: View XMRig Logs
```

#### Manual Diagnostics

```bash
# Test pool connectivity
nc -z gulf.moneroocean.stream 10001

# Monitor system resources
top -pid $(pgrep xmrig)

# Check XMRig logs
tail -f xmrig.log

# Validate configuration
python -c "import json; print(json.load(open('config.json')))"
```

#### Network Troubleshooting

```bash
# Test basic connectivity
ping gulf.moneroocean.stream

# Check DNS resolution
nslookup gulf.moneroocean.stream

# Test specific port
telnet gulf.moneroocean.stream 10001
```

### Getting Help

1. **Check Logs**: Use option 9 to view detailed XMRig output
2. **Run Diagnostics**: Use options 10 and 11 for automated troubleshooting
3. **Verify Setup**: Ensure all prerequisites are met
4. **Test Configuration**: Try different pools and settings

## 📊 Performance Optimization

### Hardware Optimization

#### CPU Configuration

| CPU Type | Optimal Threads | Priority | Notes |
|----------|-----------------|----------|-------|
| **Intel i3/i5** | 2-4 threads | 2-3 | Balance performance |
| **Intel i7/i9** | 4-8 threads | 1-2 | High performance |
| **AMD Ryzen 5** | 6-8 threads | 1-2 | Excellent multithreading |
| **AMD Ryzen 7/9** | 8-12 threads | 0-1 | Maximum throughput |
| **Apple M1/M2** | 4-6 threads | 2-3 | Thermal considerations |

#### Memory Requirements

- **Minimum**: 512MB RAM
- **Recommended**: 1GB+ RAM
- **Huge Pages**: Enable for 5-10% performance boost

### Software Optimization

#### XMRig Fine-tuning

```json
{
  "cpu": {
    "huge-pages": true,
    "hw-aes": null,
    "priority": 1,
    "memory-pool": false,
    "max-threads-hint": 100,
    "asm": "auto"
  },
  "randomx": {
    "mode": "auto",
    "1gb-pages": false,
    "rdmsr": true,
    "wrmsr": false,
    "cache_qos": false
  }
}
```

#### Pool Optimization

- **Geographic Selection**: Choose geographically close pools
- **Load Balancing**: Use pools with multiple servers
- **Fee Analysis**: Compare fee vs. reliability trade-offs
- **Payout Frequency**: Consider your liquidity needs

### System Optimization

#### macOS Optimization

```bash
# Disable App Nap for better mining performance
defaults write -g NSAppSleepDisabled -bool true

# Monitor CPU temperature
sudo powermetrics --samplers smc | grep -i "CPU die temperature"
```

#### Linux Optimization

```bash
# Enable huge pages
echo 128 > /proc/sys/vm/nr_hugepages

# Set CPU governor to performance
cpupower frequency-set -g performance

# Monitor with htop
htop
```

#### Windows Optimization

- Set power plan to "High Performance"
- Disable Windows Defender real-time protection for mining folder
- Use Process Lasso for CPU affinity management
- Monitor with Task Manager or HWiNFO

### Performance Monitoring

#### Key Metrics

- **Hashrate Stability**: Consistent performance over time
- **Acceptance Rate**: >95% indicates good pool connection
- **System Temperature**: Keep CPU <80°C
- **Power Efficiency**: Hashes per watt consumed

#### Benchmarking

```bash
# Run performance test
timeout 300 ./xmrig -c config.json

# Compare different configurations
# Test with different thread counts
# Monitor hashrate stability
```

### Advanced Techniques

#### CPU Affinity

Control which CPU cores are used for mining:

```bash
# Linux: Use taskset
taskset -c 0-7 ./xmrig -c config.json

# Windows: Use Process Explorer or PowerShell
# Set process affinity via Task Manager
```

#### NUMA Optimization

For multi-socket systems:

```json
{
  "cpu": {
    "huge-pages": true,
    "hw-aes": null
  },
  "randomx": {
    "numa": true
  }
}
```

## 🔒 Security & Privacy

### Wallet Security

#### Best Practices

- **Dedicated Mining Wallet**: Use separate address from main holdings
- **Cold Storage**: Move mined coins to secure wallet regularly
- **Address Reuse**: Never reuse mining addresses
- **Private Keys**: Never store private keys on mining machines

#### Privacy Considerations

- **Pool Selection**: Choose privacy-focused pools (P2Pool)
- **Network Traffic**: Mining traffic is public but not directly traceable
- **Local Storage**: Configuration stored locally only
- **No Telemetry**: Application sends no data externally

### System Security

#### Mining Machine Hardening

```bash
# Use strong passwords
# Keep system updated
# Use firewall (allow mining ports)
# Disable unnecessary services
# Use antivirus software
```

#### Network Security

- Use VPN for additional privacy (optional)
- Avoid mining on public WiFi
- Monitor for unauthorized access
- Use strong router passwords

### Operational Security

#### Data Protection

- Encrypt sensitive files if storing locally
- Use secure deletion for old wallet files
- Backup configurations securely
- Never share mining profits data

#### Incident Response

- Monitor for unusual hashrate drops
- Check logs for suspicious activity
- Verify wallet balances regularly
- Have backup mining setups ready

## 🤝 Contributing

### Development Setup

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/monero-mining-controller.git
cd monero-mining-controller

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # if available

# Run tests
python -m pytest

# Start development
python mining_controller.py
```

### Code Standards

- **Python**: PEP 8 compliant
- **Documentation**: Comprehensive docstrings
- **Error Handling**: Graceful failure with user feedback
- **Cross-Platform**: Test on macOS, Linux, and Windows

### Feature Requests

1. Check existing issues for duplicates
2. Provide detailed use case description
3. Include system information and XMRig version
4. Suggest implementation approach if possible

### Bug Reports

**Required Information:**
- Operating system and version
- Python version
- XMRig version
- Full error messages and logs
- Steps to reproduce
- Expected vs. actual behavior

### Pull Request Process

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request with detailed description

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-Party Components

- **XMRig**: GPLv3 License
- **Rich**: MIT License
- **psutil**: BSD License

### Disclaimer

This software is provided "as is" without warranty. Cryptocurrency mining involves financial risk. Always verify transactions and use secure practices. Mining performance depends on hardware capabilities and market conditions.


## Advanced Usage

### Custom Pool Configuration
Select option 1 in the menu, then choose "Enter custom pool details" to add your own pool.

### Manual Configuration
Edit `config.json` directly for advanced XMRig settings, then restart mining.

### Command Line Usage
```bash
# Direct XMRig usage (bypassing the controller)
./xmrig -c config.json
```

## Performance Tips

1. **Optimal Thread Count**: Usually 50-75% of available cores
2. **Priority Settings**: Start with 3, lower for more performance
3. **Pool Selection**: Consider fees vs. reliability
4. **System Resources**: Keep 20-30% CPU free for system responsiveness

## Legal and Ethical Notes

- Mining cryptocurrency is legal in most jurisdictions
- Be aware of electricity costs and environmental impact
- Consider supporting mining pools that contribute to Monero development
- Always use your own wallet addresses

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all prerequisites are met
3. Test with different pool configurations
4. Ensure stable internet connection

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the mining controller.

## License

This project is open source. Please check individual component licenses (XMRig, Python libraries).

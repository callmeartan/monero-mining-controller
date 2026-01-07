# 🚀 Monero Mining Controller

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> A professional terminal application for controlling XMRig Monero mining operations with intelligent CPU management, real-time monitoring, and performance analytics.

## ✨ Features

- **Interactive Pool Selection** - Compare 6+ popular pools with detailed metrics
- **Dynamic CPU Control** - Real-time thread and priority adjustment
- **Real-Time Dashboard** - Live statistics with auto-refresh and visual performance indicators
- **Settings Persistence** - Remembers your pool and wallet between sessions
- **Cross-Platform** - Native support for macOS, Linux, and Windows

## 📋 Requirements

- **OS**: macOS 10.15+, Linux (x86_64/ARM64), or Windows 10+
- **Python**: 3.8 or higher
- **RAM**: 512MB minimum, 1GB recommended
- **Monero Wallet**: Valid XMR address (starts with `4` or `8`)

## 🚀 Installation

### Automated Setup (Recommended)

```bash
git clone https://github.com/YOUR_USERNAME/monero-mining-controller.git
cd monero-mining-controller
python setup.py
```

The setup script will:
- Validate Python version and system compatibility
- Install required packages (`rich`, `psutil`)
- Download appropriate XMRig binary for your platform
- Create initial configuration files

### Manual Installation

```bash
pip install rich psutil
# Download XMRig from https://github.com/xmrig/xmrig/releases
# Place xmrig executable in project directory
cp config.json.example config.json
```

## ⚡ Quick Start

```bash
python mining_controller.py
```

**First-time setup:**
1. Press `1` - Select mining pool (MoneroOcean recommended)
2. Press `2` - Enter your Monero wallet address
3. Press `3` - Configure CPU threads (start with 50% of cores)
4. Press `4` - Start mining!

**Subsequent runs:** Press `4` to start mining immediately (settings are remembered)

## 📖 Menu Options

| Option | Description |
|--------|-------------|
| **1** | Select/Change Mining Pool |
| **2** | Set/Change Wallet Address |
| **3** | Configure CPU Usage |
| **4** | Start Mining |
| **5** | Stop Mining |
| **6** | Restart Mining |
| **7** | View Configuration |
| **8** | View Pool Comparison |
| **9** | View XMRig Logs |
| **10** | Check Mining Status |
| **11** | Troubleshoot Connection |
| **12** | Reset Settings |
| **0** | Exit Application |

## 🏊 Recommended Pools

| Pool | Fee | Min Payout | Best For |
|------|-----|------------|----------|
| **MoneroOcean** ⭐⭐⭐ | 0.5% | 0.003 XMR | Most users, frequent payouts |
| **SupportXMR** ⭐⭐ | 0.6% | 0.1 XMR | Beginners, community support |
| **MineXMR** ⭐⭐ | 1.0% | 0.1 XMR | Stable, established pool |
| **P2Pool** ⭐⭐ | 0% | 0.0003 XMR | Privacy-focused, decentralized |

## ⚙️ Configuration

### CPU Threads

| CPU Cores | Recommended Threads |
|-----------|-------------------|
| 2-4 | 1-2 |
| 6-8 | 3-4 |
| 10-16 | 5-8 |
| 16+ | 8-12 |

**Tip:** Start with 50% of available cores, then adjust based on system responsiveness.

### CPU Priority

| Priority | Level | Use Case |
|----------|-------|----------|
| 0 | Highest | Dedicated mining rigs |
| 1-2 | High | Primary mining machines |
| 3 | Normal | General use machines |
| 4-5 | Low | Background mining |

### Performance Tiers

- 🐌 **Slow** (< 1 KH/s)
- 👍 **Good** (1-10 KH/s)
- 🚀 **Fast** (10-100 KH/s)
- 🔥 **Blazing** (100 KH/s - 1 MH/s)
- ⚡💎 **Legendary** (≥ 1 MH/s)

## 🔧 Troubleshooting

### Connection Failed / End of File Errors

1. **Disable TLS**: Use option 11 → Press 1 to disable TLS
2. **Switch Ports**: Try alternative ports (10001, 10002, 10128)
3. **Try Different Server**: Use option 11 → Press 3 to switch servers
4. **Check Network**: Ensure stable internet connection

### XMRig Failed to Start

```bash
# Check XMRig exists and is executable
ls -la xmrig*
chmod +x xmrig  # macOS/Linux

# View current config
python mining_controller.py
# Press 7 to view configuration
```

### Low Hashrate

- Increase thread count (option 3)
- Lower CPU priority (0-2 for better performance)
- Close unnecessary applications
- Monitor CPU temperature (<80°C recommended)

### Diagnostic Tools

```bash
python mining_controller.py
# Press 10: Check Mining Status
# Press 11: Troubleshoot Connection
# Press 9: View XMRig Logs
```

### System Optimization

**macOS:**
```bash
# Disable App Nap
defaults write -g NSAppSleepDisabled -bool true
```

**Linux:**
```bash
# Enable huge pages
echo 128 > /proc/sys/vm/nr_hugepages
# Set CPU governor to performance
cpupower frequency-set -g performance
```

**Windows:**
- Set power plan to "High Performance"
- Disable Windows Defender real-time protection for mining folder

## 🔒 Security & Privacy

### Wallet Security

- ✅ Use a dedicated mining wallet
- ✅ Move mined coins to secure wallet regularly
- ❌ Never reuse addresses for different purposes
- ❌ Avoid using exchange deposit addresses for mining

### Privacy Considerations

- Choose privacy-focused pools (P2Pool)
- Configuration stored locally only
- Application sends no data externally

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-Party Components

- **XMRig**: GPLv3 License
- **Rich**: MIT License
- **psutil**: BSD License

### Disclaimer

This software is provided "as is" without warranty. Cryptocurrency mining involves financial risk. Always verify transactions and use secure practices.

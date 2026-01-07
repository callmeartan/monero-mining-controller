# 🚀 Monero Mining Controller

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A Python-based terminal application for controlling XMRig Monero mining with dynamic CPU allocation and pool selection.

## ✨ Features

- **🎯 Interactive Pool Selection**: Compare mining pools by fees, minimum payout, and features
- **⚡ Dynamic CPU Control**: Adjust CPU threads and priority in real-time
- **📊 Real-time Monitoring**: Live statistics dashboard showing hashrate, shares, and system usage
- **🛠️ Easy Configuration**: Guided setup with wallet address and pool configuration
- **🔄 Process Management**: Start, stop, and restart XMRig with updated settings
- **🌍 Cross-Platform**: Supports macOS, Linux, and Windows
- **🔒 Security-First**: No data collection, local-only operation

## 📋 Prerequisites

- **Python**: 3.8 or higher
- **Operating System**: macOS (Intel/Apple Silicon), Linux, or Windows
- **Monero Wallet**: A valid Monero wallet address

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/monero-mining-controller.git
cd monero-mining-controller
```

### 2. Run the Automated Setup
```bash
python setup.py
```

This will:
- ✅ Install Python dependencies
- ✅ Download XMRig for your platform
- ✅ Create configuration files

### 3. Configure Your Mining
```bash
python mining_controller.py
```

Follow the interactive guide to:
- Select a mining pool
- Enter your Monero wallet address
- Configure CPU usage
- Start mining!

## 📖 Usage Guide

### First Time Setup

1. **Launch the application**:
   ```bash
   python mining_controller.py
   ```

2. **Select a mining pool**:
   - Choose from 6+ popular pools (SupportXMR, MineXMR, MoneroOcean, etc.)
   - Compare fees, minimum payouts, and features
   - Option to add custom pools

3. **Enter your wallet address**:
   - Use your Monero wallet address (starts with 4...)
   - The app validates the format

4. **Configure CPU usage**:
   - Set number of CPU threads (1 to max cores)
   - Adjust CPU priority (0=highest to 5=lowest)

5. **Start mining**:
   - The app updates XMRig configuration automatically
   - Starts the mining process
   - Real-time statistics dashboard appears

### 🎯 Pool Recommendations

| Pool | Fee | Min Payout | Best For |
|------|-----|------------|----------|
| **SupportXMR** ⭐ | 0.6% | 0.1 XMR | Beginners, reliability |
| **MineXMR** ⭐ | 1.0% | 0.1 XMR | Stable mining |
| **MoneroOcean** ⭐ | 0.5% | 0.003 XMR | Frequent payouts |
| **P2Pool** ⭐ | 0% | 0.0003 XMR | Privacy-focused |
| **Nanopool** | 1.0% | 1.0 XMR | Large operations |
| **HashVault** | 0.9% | 0.5 XMR | Good balance |

### ⚙️ Interactive Controls

| Option | Description |
|--------|-------------|
| **1** | Select/Change mining pool |
| **2** | Set/Change wallet address |
| **3** | Configure CPU usage |
| **4** | Start mining |
| **5** | Stop mining |
| **6** | Restart with new settings |
| **7** | View current configuration |
| **8** | View pool comparison |
| **0** | Exit application |

## Monitoring

The application provides real-time statistics:

- **Mining Status**: Running/Stopped
- **Hashrate**: Current mining speed (H/s)
- **Shares**: Accepted/Rejected share counts
- **System Usage**: CPU and memory usage
- **Uptime**: Mining session duration

## Configuration Files

- `config.json`: XMRig configuration (auto-generated)
- `pools.json`: Pool database with comparison data
- `mining_controller.py`: Main application
- `requirements.txt`: Python dependencies

## Security Notes

- Your wallet address is stored locally in `config.json`
- Never share your configuration files
- Use a dedicated mining wallet for security
- Consider using a hardware wallet for large amounts

## Troubleshooting

### XMRig Won't Start
- Check that XMRig binary exists and is executable
- Verify wallet address format
- Ensure pool URL and port are correct
- Check macOS security settings for unsigned binaries

### Low Hashrate
- Increase CPU threads in configuration
- Lower CPU priority for more aggressive mining
- Close other CPU-intensive applications
- Ensure Mac is plugged in (prevents power management throttling)

### Pool Connection Issues
- Verify pool URL and port
- Check internet connection
- Try different pool servers
- Some pools may have geo-restrictions

### Python Errors
- Install dependencies: `pip install -r requirements.txt`
- Ensure Python 3.8+ is being used
- Check for conflicting Python installations

### Permission Errors
```bash
chmod +x xmrig
```

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

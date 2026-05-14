#!/usr/bin/env python3
"""
Monero Mining Controller - Setup Script

This script helps users set up their mining environment by:
1. Downloading XMRig for their platform
2. Creating initial configuration files
3. Installing Python dependencies
"""

import os
import sys
import platform
import subprocess
import urllib.request
import json
import shutil
from pathlib import Path

def run_command(cmd, description=""):
    """Run a command and handle errors"""
    try:
        print(f"🔧 {description}")
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        print(f"Command output: {e.stderr}")
        return False

def detect_platform():
    """Detect the platform and architecture"""
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "darwin":  # macOS
        if "arm64" in machine or "aarch64" in machine:
            return "macos-arm64"
        else:
            return "macos-x64"
    elif system == "linux":
        if "x86_64" in machine:
            return "linux-x64"
        elif "aarch64" in machine:
            return "linux-arm64"
        else:
            return "linux-x86"
    elif system == "windows":
        return "windows-x64"
    else:
        return None

def download_xmrig(platform_type):
    """Download XMRig for the detected platform"""
    print("🚀 Downloading XMRig...")

    # Get latest release info
    try:
        request = urllib.request.Request("https://api.github.com/repos/xmrig/xmrig/releases/latest")
        request.add_header("User-Agent", "Python")
        with urllib.request.urlopen(request) as response:
            release_data = json.loads(response.read().decode())
    except:
        print("❌ Could not fetch XMRig releases. Please download manually from https://github.com/xmrig/xmrig/releases")
        return False

    # Find the correct asset for our platform
    asset_name = None
    if platform_type == "macos-arm64":
        asset_name = "xmrig-6.25.0-macos-arm64.tar.gz"
    elif platform_type == "macos-x64":
        asset_name = "xmrig-6.25.0-macos-x64.tar.gz"
    elif platform_type == "linux-x64":
        asset_name = "xmrig-6.25.0-linux-x64.tar.gz"
    elif platform_type == "linux-arm64":
        asset_name = "xmrig-6.25.0-linux-arm64.tar.gz"
    elif platform_type == "windows-x64":
        asset_name = "xmrig-6.25.0-msvc-win64.zip"

    if not asset_name:
        print(f"❌ Unsupported platform: {platform_type}")
        return False

    # Find download URL
    download_url = None
    for asset in release_data.get("assets", []):
        if asset_name in asset["name"]:
            download_url = asset["browser_download_url"]
            break

    if not download_url:
        print(f"❌ Could not find download URL for {asset_name}")
        return False

    # Download the file
    filename = f"xmrig-{platform_type}.tar.gz" if platform_type != "windows-x64" else f"xmrig-{platform_type}.zip"

    try:
        print(f"📥 Downloading from: {download_url}")
        request = urllib.request.Request(download_url)
        request.add_header("User-Agent", "Python")
        with urllib.request.urlopen(request) as response, open(filename, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    except:
        print("❌ Download failed. Please download manually.")
        return False

    # Extract the archive
    print("📦 Extracting XMRig...")
    if platform_type == "windows-x64":
        import zipfile
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(".")
    else:
        run_command(f"tar -xzf {filename}", "Extracting archive")

    # Move xmrig binary to project root
    xmrig_dirs = [d for d in os.listdir(".") if d.startswith("xmrig-") and os.path.isdir(d)]
    if xmrig_dirs:
        xmrig_dir = xmrig_dirs[0]
        if os.path.exists(f"{xmrig_dir}/xmrig"):
            shutil.move(f"{xmrig_dir}/xmrig", "xmrig")
        elif os.path.exists(f"{xmrig_dir}/xmrig.exe"):
            shutil.move(f"{xmrig_dir}/xmrig.exe", "xmrig.exe")

        # Make executable on Unix systems
        if platform.system() != "Windows":
            os.chmod("xmrig", 0o755)

        # Clean up
        shutil.rmtree(xmrig_dir)
        os.remove(filename)

    print("✅ XMRig setup complete!")
    return True

def create_config():
    """Create initial config.json from example"""
    if os.path.exists("config.json.example") and not os.path.exists("config.json"):
        print("📄 Creating config.json from template...")
        shutil.copy("config.json.example", "config.json")
        print("✅ Config file created! Please edit config.json with your wallet address and pool details.")
        return True
    return False

def install_dependencies():
    """Install Python dependencies"""
    print("📦 Installing Python dependencies...")
    return run_command(f"{sys.executable} -m pip install -r requirements.txt", "Installing dependencies")

def main():
    print("🚀 Monero Mining Controller Setup")
    print("=" * 40)

    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        sys.exit(1)

    # Detect platform
    platform_type = detect_platform()
    if not platform_type:
        print("❌ Unsupported platform")
        sys.exit(1)

    print(f"✅ Detected platform: {platform_type}")

    # Create config if needed
    create_config()

    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)

    # Download XMRig
    if not os.path.exists("xmrig") and not os.path.exists("xmrig.exe"):
        if not download_xmrig(platform_type):
            print("❌ Failed to download XMRig")
            print("You can download it manually from: https://github.com/xmrig/xmrig/releases")
            sys.exit(1)
    else:
        print("✅ XMRig already exists")

    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    print("1. Edit config.json with your Monero wallet address")
    print("2. Run: python mining_controller.py")
    print("3. Follow the interactive setup guide")

if __name__ == "__main__":
    main()

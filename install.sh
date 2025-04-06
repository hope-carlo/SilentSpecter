#!/bin/bash
echo "[*] Installing SilentSpecter dependencies..."
sudo apt update
sudo apt install -y python3-pip python3-opencv
pip3 install -r requirements.txt
echo "[+] Installation complete. Run 'python3 server.py' to start."

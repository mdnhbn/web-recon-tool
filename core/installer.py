# core/installer.py
import subprocess
import sys

def install_missing_tools():
    """যেসব টুল মিসিং রয়েছে, সেগুলো ওয়ান-ক্লিক ইনস্টল করার ফাংশন"""
    print("[*] Starting automated installation of missing tools...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("[+] Python requirements installed successfully.")
    except Exception as e:
        print(f"[-] Error installing python requirements: {e}")

    go_tools = [
        "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
        "github.com/projectdiscovery/dnsx/cmd/dnsx@latest",
        "github.com/projectdiscovery/httpx/cmd/httpx@latest",
        "github.com/projectdiscovery/katana/cmd/katana@latest",
        "github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest",
        "github.com/ffuf/ffuf/v2@latest"
    ]

    for tool in go_tools:
        try:
            print(f"[*] Installing {tool}...")
            subprocess.run(["go", "install", "-v", tool], check=True)
        except Exception as e:
            print(f"[-] Could not install {tool}: {e}")
    
    print("[+] One-click installation process completed!")

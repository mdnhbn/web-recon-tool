# core/runner.py
import subprocess
import os
from utils.config import OUTPUT_DIR

def run_recon_pipeline(target, log_callback=None):
    """
    Phase 0 থেকে Phase 9 পর্যন্ত রিকন পাইপলাইন পরিচালনা করার মূল ম্যানেজার।
    কোনো ফেজে সমস্যা হলেও যেন বাকি ফেজগুলো থেমে না যায়, তা নিশ্চিত করে।
    """
    results = {}
    subdomains_file = os.path.join(OUTPUT_DIR, f"{target}_subdomains.txt")
    live_hosts_file = os.path.join(OUTPUT_DIR, f"{target}_live_hosts.txt")
    
    # Phase 2: Subdomain Enumeration (Subfinder)
    if log_callback:
        log_callback(f"[*] [Phase 2] Finding subdomains for {target} using Subfinder...\n")
    try:
        cmd = ["subfinder", "-d", target, "-silent", "-o", subdomains_file]
        subprocess.run(cmd, check=True, timeout=120)
        results["Subdomain Enumeration"] = f"Completed. Saved in {subdomains_file}"
        if log_callback: log_callback(f"[+] Subdomain enumeration successful!\n")
    except Exception as e:
        results["Subdomain Enumeration"] = f"Skipped/Error: {e}"
        if log_callback: log_callback(f"[-] Subfinder error: {e}\n")

    # Phase 3: Active Probing (Httpx)
    if log_callback:
        log_callback(f"[*] [Phase 3] Verifying live hosts using Httpx...\n")
    try:
        if os.path.exists(subdomains_file) and os.path.getsize(subdomains_file) > 0:
            cmd = ["httpx", "-l", subdomains_file, "-title", "-status-code", "-silent", "-o", live_hosts_file]
            subprocess.run(cmd, check=True, timeout=120)
            results["Active Probing"] = f"Completed. Live hosts saved in {live_hosts_file}"
            if log_callback: log_callback(f"[+] Live host probing successful!\n")
        else:
            results["Active Probing"] = "Skipped: No subdomains found to probe."
            if log_callback: log_callback(f"[-] No subdomains found to probe.\n")
    except Exception as e:
        results["Active Probing"] = f"Skipped/Error: {e}"
        if log_callback: log_callback(f"[-] Httpx error: {e}\n")
        
    return results

# core/checker.py
import shutil

def check_tool_installed(tool_name):
    """সিস্টেমে নির্দিষ্ট টুল (যেমন: subfinder, httpx, nmap ইত্যাদি) ইনস্টল আছে কি না চেক করে"""
    return shutil.which(tool_name) is not None

def get_all_tools_status():
    """সমস্ত প্রয়োজনীয় টুলের ইনস্টল স্ট্যাটাস চেক করে একটি ডিকশনারি রিটার্ন করবে"""
    tools = {
        "Go": "go",
        "Python3": "python3",
        "Git": "git",
        "Subfinder": "subfinder",
        "Dnsx": "dnsx",
        "Httpx": "httpx",
        "Katana": "katana",
        "Nuclei": "nuclei",
        "Sqlmap": "sqlmap",
        "Nmap": "nmap",
        "Ffuf": "ffuf"
    }
    
    status = {}
    for name, cmd in tools.items():
        status[name] = check_tool_installed(cmd)
    return status

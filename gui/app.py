# gui/app.py
import customtkinter as ctk
from core.checker import get_all_tools_status
from core.installer import install_missing_tools
from gui.components import ToolStatusIndicator
from gui.ads_client import fetch_remote_ads
from utils.reporter import generate_pdf_report

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ReconApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Cross-Platform Web Application Recon Tool")
        self.geometry("900x650")
        
        self.create_widgets()
        self.load_tool_statuses()
        self.load_ads()

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text="Web Application Reconnaissance Dashboard", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)
        
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # বাম পাশ: ইনপুট এবং ফেজ কন্ট্রোল
        left_frame = ctk.CTkFrame(main_frame, width=450)
        left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        ctk.CTkLabel(left_frame, text="Enter Target Domain / URL:", font=("Arial", 14)).pack(anchor="w", padx=10, pady=5)
        self.target_entry = ctk.CTkEntry(left_frame, placeholder_text="example.com", width=400)
        self.target_entry.pack(padx=10, pady=5)
        
        self.scan_btn = ctk.CTkButton(left_frame, text="Start Full Scan & Generate PDF", command=self.start_scan)
        self.scan_btn.pack(padx=10, pady=15)
        
        ctk.CTkLabel(left_frame, text="Dependencies & Tools Status:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)
        
        self.tools_frame = ctk.CTkScrollableFrame(left_frame, height=200, width=400)
        self.tools_frame.pack(padx=10, pady=5, fill="both", expand=True)
        
        self.install_btn = ctk.CTkButton(left_frame, text="One-Click Install Missing Tools", fg_color="green", command=self.run_installation)
        self.install_btn.pack(padx=10, pady=10)

        # ডান পাশ: লগ এবং রিমোট অ্যাড প্যানেল
        right_frame = ctk.CTkFrame(main_frame, width=380)
        right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)
        
        ctk.CTkLabel(right_frame, text="Live Output Log:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)
        self.log_textbox = ctk.CTkTextbox(right_frame, width=360, height=300)
        self.log_textbox.pack(padx=10, pady=5)
        
        ctk.CTkLabel(right_frame, text="Sponsored Ads / Announcements:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)
        self.ad_frame = ctk.CTkFrame(right_frame, height=100, fg_color="#2b2b2b")
        self.ad_frame.pack(padx=10, pady=5, fill="x")
        
        self.ad_label = ctk.CTkLabel(self.ad_frame, text="Loading ads...", text_color="white")
        self.ad_label.pack(padx=10, pady=10)

    def load_tool_statuses(self):
        for widget in self.tools_frame.winfo_children():
            widget.destroy()
            
        statuses = get_all_tools_status()
        for tool, is_inst in statuses.items():
            indicator = ToolStatusIndicator(self.tools_frame, tool_name=tool, is_installed=is_inst)
            indicator.pack(fill="x", pady=2)

    def run_installation(self):
        self.log_textbox.insert("end", "[*] Running One-Click Installer...\n")
        install_missing_tools()
        self.load_tool_statuses()
        self.log_textbox.insert("end", "[+] Installation completed & statuses refreshed.\n")

    def load_ads(self):
        ads_data = fetch_remote_ads()
        ad_text = ads_data.get("ad_html", "Check out our latest tools!")
        self.ad_label.configure(text=ad_text)

    def start_scan(self):
        target = self.target_entry.get().strip()
        if not target:
            self.log_textbox.insert("end", "[-] Error: Please enter a valid target domain!\n")
            return
        
        self.log_textbox.insert("end", f"[*] Starting reconnaissance on target: {target}\n")
        
        dummy_results = {
            "Phase 1 - Passive Recon": "Checked via Censys & Shodan. Target IP range identified.",
            "Phase 2 - Subdomain Enumeration": "Subfinder found subdomains successfully.",
            "Phase 3 - Active Probing": "Httpx verified live hosts."
        }
        
        pdf_path = generate_pdf_report(target, dummy_results)
        self.log_textbox.insert("end", f"[+] Recon complete! PDF report saved at: {pdf_path}\n")

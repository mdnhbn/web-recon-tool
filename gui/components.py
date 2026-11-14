# gui/components.py
import customtkinter as ctk

class ToolStatusIndicator(ctk.CTkFrame):
    """টুলের নামের পাশে গ্রিন/রেড লাইট (স্ট্যাটাস) দেখানোর জন্য কাস্টম কম্পোনেন্ট"""
    def __init__(self, master, tool_name, is_installed, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        self.label = ctk.CTkLabel(self, text=tool_name, font=("Arial", 12))
        self.label.pack(side="left", padx=5)
        
        # লাইট কালার: ইনস্টল থাকলে সবুজ (green), না থাকলে লাল (red)
        color = "green" if is_installed else "red"
        self.light = ctk.CTkCanvas(self, width=15, height=15, highlightthickness=0)
        self.light.pack(side="right", padx=5)
        self.light.create_oval(2, 2, 13, 13, fill=color, outline=color)

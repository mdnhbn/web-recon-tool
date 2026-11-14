# utils/reporter.py
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from utils.config import OUTPUT_DIR

def generate_pdf_report(target_domain, recon_results):
    """স্ক্যান ফলাফল থেকে একটি সুন্দর PDF রিপোর্ট জেনারেট করবে"""
    pdf_filename = os.path.join(OUTPUT_DIR, f"{target_domain}_recon_report.pdf")
    
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter
    
    # হেডার
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, f"Web Application Reconnaissance Report")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 75, f"Target Domain: {target_domain}")
    
    # কন্টেন্ট প্রিন্ট করা
    y = height - 110
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Scan Findings:")
    
    y -= 30
    c.setFont("Helvetica", 10)
    
    for phase_name, data in recon_results.items():
        if y < 50:
            c.showPage()
            y = height - 50
        c.drawString(50, y, f"[{phase_name}]")
        y -= 15
        c.drawString(70, y, f"Result: {str(data)[:80]}...")
        y -= 25
        
    c.save()
    return pdf_filename

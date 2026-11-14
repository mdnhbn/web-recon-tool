# gui/ads_client.py
import requests
from utils.config import REMOTE_API_URL

def fetch_remote_ads():
    """
    রিমোট অ্যাডমিন সার্ভার থেকে অ্যাড ডেটা ফেচ করে নিয়ে আসার ফাংশন।
    কোনো কারণে সার্ভার ডাউন থাকলে ডিফল্ট বা এম্টি রেসপন্স রিটার্ন করবে।
    """
    try:
        response = requests.get(REMOTE_API_URL, timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Ad fetch error: {e}")
    
    # ফলব্যাক বা ডিফল্ট অ্যাড ডাটা (সার্ভার না পেলে দেখানোর জন্য)
    return {
        "ad_html": "Sponsored: Check out our premium cyber tools!",
        "status": "offline"
    }

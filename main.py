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
    from random import choice
    from colorama import Fore
    from pypresence import *
    from bs4 import BeautifulSoup
    from datetime import datetime
except ImportError:
    os.system('pip install requests colorama psutil datetime bs4 pypresence')
    print('Please re-run the program and install requirements.txt')
    time.sleep(5)
    exit()

colorama.init()

valids = 0
invalids = 0
totals = 0

def proxy_generator():
    response = requests.get("https://sslproxies.org/")
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

client_id = '926434489054400522'
RPC = Presence(client_id, pipe=0)
RPC.connect()

def rpc():
    start_time = time.time()

    while True:
        cpu_per = round(psutil.cpu_percent(),1)
        mem_per = round(psutil.virtual_memory().percent,1)
        RPC.update(start=start_time, details="RAM: "+str(mem_per)+"%", state="CPU: "+str(cpu_per)+"%", large_image="nitro_512x512", small_image="dc", large_text="Generating...", small_text="v1.6", buttons=[{"label": "GitHub", "url": "https://github.com/ReflexTheLegend/Nitro-Generator-N-Checker"}, {"label": "Download", "url": "https://github.com/ReflexTheLegend/Nitro-Generator-N-Checker/releases/latest"},])  # Set the presence
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

def main():
    global valids
    global invalids
    global totals
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
                 }R3FL3X#1337{Fore.LIGHTBLACK_EX} | Licenced under {Fore.GREEN}MIT Licence{Fore.LIGHTBLUE_EX}
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

        print(f"{Fore.YELLOW}Generated {num} codes | Time taken: {time.time() - start}s\n")

    with open("Nitro Codes.txt") as file:
        for line in file.readlines():
            nitro = line.strip("\n")

            url = "https://discordapp.com/api/v9/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

            r = data_scraper('http', url)

            if r == '<Response [200]>':
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"{Fore.GREEN}{current_time} - [ VALID ] | {nitro} \n")
                valids+=1
                totals+=1
                break
            elif r == '<Response [429]>':
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"{Fore.YELLOW}{current_time} - [ RATE LIMIT ] | {nitro} \n")
                valids+=1
                totals+=1
                time.sleep(1)
            else:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"{Fore.RED}{current_time} - [ INVALID ] | {nitro}")
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

if __name__ == "__rpc__":
    rpc()

t1=threading.Thread(target=rpc)
t2=threading.Thread(target=main)
if "discord.exe" in (i.name() for i in psutil.process_iter()):
    t1.start()
    t2.start()
else:
    t2.start()

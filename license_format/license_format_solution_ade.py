import os
import re

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'

print('*'*25)
pattern = r'^[1-9]{1}[^a-z,I,O]{3}[0-9]{3}$'

def valid_license(line):
    if len(line) != 7:
        return
    if len(set(line[-3:])) < 2:
        return
    if not re.match(pattern,line):
        return
    return line

with open(path,'r') as file:
    for line in file:
        line = line.strip()
        result = valid_license(line)

        if result is not None:
            print(f'Valid   ✅: {line}')
        else:
            print(f'Invalid ❌: {line}')
            
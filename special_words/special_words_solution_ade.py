import os
import re

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'

pattern = r'^he[a-z]*(er)$|^her[a-z]*$' 

print('*'*30)
with open (path,'r') as file:
    for line in file:
        line = line.strip()
        if re.match(pattern,line,re.IGNORECASE):
            print(f'Matched  ✅: {line}')
        else:
            print(f'No Match ❌: {line}')
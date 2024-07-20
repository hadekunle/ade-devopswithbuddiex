import os
import re

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'

pattern = r'^he[A-Za-z]*(er)|^her' 

with open (path,'r') as file:
    for line in file:
        line = line.strip()
        if re.match(pattern,line):
            print(line)

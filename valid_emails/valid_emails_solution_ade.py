import os
import re

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'

pattern = r'^[A-Za-z\d][A-Za-z\d-]*@\w+\.(com|net|edu|gov)$'

with open (path,'r') as file:
    next(file)
    for line in file:
        first, last, email = line.strip().split(" ",2)
        if re.match(pattern,email):
            print(email)
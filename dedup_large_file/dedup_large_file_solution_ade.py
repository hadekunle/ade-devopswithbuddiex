import os

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'
path2 = f'{directory}/file_ade'

unique = []
with open(path,'r') as file:
    for line in file:
        line = line.strip()
        if line not in unique or line=='':
            unique.append(line)

with open(path2,'w') as file:
    for i in unique:
        file.write(f'{i}\n')
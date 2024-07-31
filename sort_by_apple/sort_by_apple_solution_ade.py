import os

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/new_file'
count_list=[]

with open(path,'r') as file:
    for line in file:
        count = line.strip().split(',').count('apple')
        count_list.append((count,line))
sorted_sites = sorted(count_list, key=lambda kv: (kv[0]),reverse=True)

with open(f'{directory}/ade_file.txt','w') as file:
    for count,line in sorted_sites:
        file.write(f'{count}:{line}')
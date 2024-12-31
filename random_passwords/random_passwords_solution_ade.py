import os
import re

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'

pattern = r'^[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}$'
unique = set()
seen = set()
with open(path,'r') as file:
    for line in file:
        line = line.strip()
        if re.match(pattern,line):
            if line in seen:
                if line in unique:
                    unique.discard(line)
            else:
                seen.add(line)
                unique.add(line)

print(*unique ,sep='\n')



# unique = [x for x in unique if unique.count(x)==1]
# unique = dict(filter(lambda x:x[1]==1, unique.items()))
# unique = {k:v for k,v in unique.items() if v==1}
import os

os.system('clear')

directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'
count_dict = {} #{key,value}

with open(path,'r') as file:
    content = file.read().split()

    for word in content:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word]+= 1


sorted_sites = sorted(count_dict.items(), key=lambda kv: (kv[1]),reverse=True)
third_place_value = sorted_sites[2][1]

for key,value in sorted_sites:
    if value >= third_place_value:
        print(f'{key}, {value}')

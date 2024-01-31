from os import system
from pprint import pprint

system("clear")

company_main_line = "(444) 123-1233"
dict_info_a = {}    
with open ('fileA','r') as file:
    for line in file: 
        line = line.strip()
        username = line.split('@')[0]
        email = line.split(' ')[0]
        area_code, phone_suffix = line.split(' ')[-2:]
        phone_number = f"{area_code} {phone_suffix}"
        dict_info_a[username] = {
                                    'email' :email,
                                    'phone_number' : phone_number
                                }
# pprint(dict_info_a)

with open ('fileB','r') as file:
    next(file)
    for line in file:
        line = line.strip()
        username = line.split(' ')[0]
        is_active = line.split(' ')[-1].title()

        if is_active == 'Yes':
            if username in dict_info_a.keys():
                print(f'{username} {dict_info_a[username]["phone_number"]}')
            else:
                print(f'{username} {company_main_line}')
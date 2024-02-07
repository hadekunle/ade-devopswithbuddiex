from os import path, system
from pprint import pprint
from sys import argv as argument

system("clear")

company_main_line = "(444) 123-1233"

def active_users(all_users, check_active_users):
    dict_info_a = {}    
    with open (all_users,'r') as file:
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

    with open (check_active_users,'r') as file:
        next(file)
        line = line.strip()
        username = line.split(' ')[0]
        is_active = line.split(' ')[-1].title()

        if is_active == 'Yes':
            if username in dict_info_a.keys():
                print(f'{username} {dict_info_a[username]["phone_number"]}')
            else:
                print(f'{username} {company_main_line}')

def main():
    if len(argument) != 3:
        error_message="\nDon't forget to pass in only 2 files\nCompany Directory First\nThen Check List Second"
        raise ValueError(f"{error_message}")

    all_users = argument[1]
    check_active_users = argument[2]

    if not path.exists(all_users):
        raise FileNotFoundError(f"{all_users} does not exist")
    if not path.exists(check_active_users):
        raise FileNotFoundError(f"{all_users} does not exist")

    active_users(all_users,check_active_users)

if __name__ == "__main__":
    main()
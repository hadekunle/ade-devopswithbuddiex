import re
from os import path, system
from sys import argv as argument

system('clear')

regex_1 = r'([0-9A-F]{2}:){5}[0-9A-F]{2}'

mac_address_pattern = f'{regex_1}'

def main():
    name_dict={}
    with open ('file','r') as file:
        header = f'{"MAC address".center(14)}'
        print(f'{header}')
        print(f"{'-'*30}")
        for line_number,line in enumerate(file, start=1):
            mac_address = False
            try:
                mac_address = re.findall(mac_address_pattern, line)[0]
                print(f'{line.strip()}')
            except:
                print(f'No match on line {line_number}')

         
if __name__ == "__main__":
    main()
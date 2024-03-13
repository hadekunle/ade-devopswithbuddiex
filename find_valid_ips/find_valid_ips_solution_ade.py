import re
from os import path, system
from sys import argv as argument

system('clear')

regex_1 = r'([0-2]*[0-9]*[0-9]*\.){3}([0-2]*[0-9]*[0-9]*)\s'  # 123.456.789.123

valid_ip_pattern = f'{regex_1}'

def main():
    name_dict={}
    with open ('file','r') as file:
        header = f'{"IP address".center(14)}'
        print(f'{header}')
        print(f"{'-'*30}")
        for line_number,line in enumerate(file, start=1):
            valid_ip = False
            try:
                valid_ip = re.findall(valid_ip_pattern, line)[0]
                print(f'{line.strip()}')
            except:
                print(f'No match on line {line_number}')

         
if __name__ == "__main__":
    main()
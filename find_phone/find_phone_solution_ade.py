import re
from os import path, system
from sys import argv as argument

system('clear')

regex_1 = r'\b\s\d{3}-\d{3}-\d{4}\b'         # xxx-xxx-xxxx
regex_2 = r'\b\s\d{3}\.\d{3}\.\d{4}\b'       # xxx.xxx.xxxx
regex_3 = r'\b\s\d{3}\s\d{3}\s\d{4}\b'       # xxx xxx xxxx
regex_4 = r'\b\s\(\d{3}\)\s\d{3}\s\d{4}\b'   # (xxx) xxx xxxx
regex_5 = r'\b\s\(\d{3}\)\s\d{3}-\d{4}\b'    # (xxx) xxx-xxxx

phone_pattern = f'{regex_1}|{regex_2}|{regex_3}|{regex_4}|{regex_5}'

def main():
    name_dict={}
    with open ('file','r') as file:
        header = f'{"Name".center(15)}{"Phone_num".center(14)}'
        print(f'{header}')
        print(f"{'-'*30}")
        for line_number,line in enumerate(file, start=1):
            Phone_num = False
            try:
                Phone_num = re.findall(phone_pattern, line)[0]
                print(f'{line.strip()}')
            except:
                print(f'No match on line {line_number}')

            # name_dict[Username] =  {'Phone_num' : Phone_num  }

    # sorted_running_list = sorted(name_dict.items(), key=lambda x: x[0])

if __name__ == "__main__":
    main()
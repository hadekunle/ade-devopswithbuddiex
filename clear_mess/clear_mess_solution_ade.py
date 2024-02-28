import re
from datetime import datetime, timedelta
from os import path, system
from sys import argv as argument

system('clear')
time_fmt = '%H:%M:%S %m/%d/%Y'

def main():
    name_dict={}
    with open ('file','r') as file:
        header = f'{"Username".center(20)}|{"Phone_num".center(20)}|{"Start_date".center(20)} '
        # print(f"{'':-<62}")
        print(f"{'-'*62}")
        for line_number,line in enumerate(file, start=1):
            try:
                Username   = re.findall(r'[A-Z]*[a-z]+',line)[0]
            except:
                Username = f'No match on line {line_number}'
            try:
                Phone_num  = re.findall(r'\d{3}-\d{3}-\d{4}',line)[0]
            except:
                Phone_num = 'No match'
            try:
                Start_date = re.findall(r'\d{2}/\d{2}/\d{4}',line)[0]
            except:
                Start_date = 'No match'
                
            name_dict[Username] =  {'Phone_num' : Phone_num , 'Start_date' : Start_date }

    sorted_running_list = sorted(name_dict.items(), key=lambda x: x[0])

    with open ('clear_mess_report','w') as file:
        file.write(f'{header}\n')
        file.write('-'*64)
        file.write('\n')
        for key,value in sorted_running_list:
            report = f"{key.center(20)}|{value['Phone_num'].center(20)}|{value['Start_date'].center(20)}"
            file.write(f'{report}\n')


if __name__ == "__main__":
    main()
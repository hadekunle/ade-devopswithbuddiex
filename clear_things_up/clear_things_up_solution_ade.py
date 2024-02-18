from collections import OrderedDict
from datetime import datetime, timedelta
from os import path, system
from pprint import pprint
from sys import argv as argument

system('clear')
time_fmt = '%H:%M:%S %m/%d/%Y'

start_parsed_data={}
end_parsed_data={}
pid_list=set()

def calculate_interval(start: str,end: str):
    start_time = datetime.strptime(start, time_fmt)
    end_time = datetime.strptime(end, time_fmt)
    time_diff = end_time - start_time
    return time_diff

def parser(check_file='file'):
    with open (check_file,'r') as file:
        next(file)
        for line in file: 
            parts = line.strip().split()
            time = f"{parts[0]} {parts[1]}"
            pid, action = parts[2], parts[3]
            pid_list.add(pid)
            
            if action.lower()=='start':
                start_parsed_data[pid] = time
            elif action.lower()=='end':
                end_parsed_data[pid] = time

def report(start_dict:dict, end_dict:dict):
    for each_pid in sorted(pid_list):
        start_time = start_dict[each_pid]
        end_time = end_dict[each_pid]
        print(f'{each_pid} {calculate_interval(start_time,end_time)}')

def main():
    if len(argument) > 2:
        error_message="\nDon't forget to pass in the log file ONLY else pass nothing"
        raise ValueError(f"{error_message}")
    elif len(argument) == 2:
        check_file = argument[1]
        if not path.exists(check_file):
            raise FileNotFoundError(f"{check_file} does not exist")
        parser(check_file)
    else:
        parser()
    
    report(start_parsed_data,end_parsed_data)

if __name__ == "__main__":
    main()
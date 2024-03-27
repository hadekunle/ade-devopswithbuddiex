from datetime import datetime, timedelta
from os import path, system
from pprint import pprint
from sys import argv as argument

#system('clear') # Don't worry abourrit 
time_fmt = '%H:%M:%S %m/%d/%Y'

def parser(check_file='binary_queue_backup',report_file='binary_queue_ade'):
    with open (check_file,'r') as file:
        file = file.readlines()[1:]
        queue_list= [each.strip() for each in file if each.strip().split()[-1] in ('queued')]
        running_list= [each.strip() for each in file if each.strip().split()[-1] in ('running')]
    
    sorted_queue_list = sorted(queue_list,key=lambda x: f'{datetime.strptime(f"{x.split()[1]} {x.split()[2]}", time_fmt)}')
    sorted_running_list = sorted(running_list,key=lambda x: f'{datetime.strptime(f"{x.split()[1]} {x.split()[2]}", time_fmt)}')
    combined_list = sorted_queue_list + sorted_running_list
    
    with open (report_file,'w') as file:
        file.write('binary created_at status\n')
        for i in combined_list:
            file.write(f'{i}\n')
    return combined_list

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

if __name__ == "__main__":
    main()

# This should be in the unittest as well? why is that?
# if __name__ == "__main__":
#     unittest.main()


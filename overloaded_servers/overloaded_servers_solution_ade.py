from datetime import datetime, timedelta
from os import path, system
from pprint import pprint
from sys import argv as argument

system('clear')

def overload(log_file):
    with open (log_file,'r') as file:
        warn_level = False
        for line in file: 
            parts = line.strip().split()
            server, date, time, cpu_load, ram_load, disk_usage = parts

            if float(cpu_load) >= 0.80 and (not warn_level):
                warn_level = True
                start_date, start_time = date , time 
            elif float(cpu_load) >= 0.80 and warn_level:
                print(f'Warning: server {server} CPU load is over 80% from {start_date} {start_time} to {date} {time}')
                start_date, start_time = date , time 
            else:
                warn_level = False

# Add checks to see if server is same and time is one minute difference...
# expected_average = timedelta(hours=11, minutes=9, seconds=35, microseconds=600000)


def main():
    if len(argument) > 2:
        error_message="\nDon't forget to pass in the log file ONLY"
        raise ValueError(f"{error_message}")
    elif len(argument) == 2 :
        log_file = argument[1]
    else:
        log_file = './overloaded_servers/log'
     
    if not path.exists(log_file):
        raise FileNotFoundError(f"{log_file} does not exist")

    overload(log_file)

        
if __name__ == "__main__":
    main()
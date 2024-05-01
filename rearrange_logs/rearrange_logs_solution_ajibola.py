import sys
import os 
import re

pattern = '^log(?:.*)?$'

def extract_log_files(input_directory="."):
    log_files = []
    for root, dirs, files in os.walk(input_directory):
        for name in files:
            if re.match(pattern, name, re.IGNORECASE):
                full_path = os.path.join(root, name)
                log_files.append(full_path)
    return log_files


def extract_logs(input_directory="."):
    get_log = {}
    set_log = {}
    add_log = {}

    log_files = extract_log_files(input_directory)
    for file in log_files:
        with open(file, 'r') as log_lines:
            for line in log_lines:
                line = line.strip()
                time, date, function_name,  *parameters= line.split()
                if function_name == "Get" and date not in get_log:
                    get_log [date] = [[line], 1]
                elif function_name == "Get" and date in get_log:
                    get_log[date][0].append(line)
                    get_log[date][1] += 1
                
                if function_name == "Set" and date not in set_log:
                    set_log [date] = [[line], 1]
                elif function_name == "Set" and date in set_log:
                    set_log[date][0].append(line)
                    set_log[date][1] += 1
                
                if function_name == "Add" and date not in add_log:
                    add_log [date] = [[line], 1]
                elif function_name == "Add" and date in add_log:
                    add_log[date][0].append(line)
                    add_log[date][1] += 1
    return get_log, set_log, add_log

def write_logs():
    get_log, set_log, add_log = extract_logs(input_directory=".")
    with open('get_log_aji', 'w') as log_line:
        with open('stats_log_aji', 'a') as stat_line:
            stat_line.write('Get\n')
            for date, value in get_log.items():
                for line in value[0]:
                    log_line.write(f'{line}\n')
                stat_line.write(f'{date} {value[1]}\n')

    with open('set_log_aji', 'w') as log_line:
        with open('stats_log_aji', 'a') as stat_line:
            stat_line.write('Set\n')
            for date, value in set_log.items():
                for line in value[0]:
                    log_line.write(f'{line}\n')
                stat_line.write(f'{date} {value[1]}\n')

    with open('add_log_aji', 'w') as log_line:
        with open('stats_log_aji', 'a') as stat_line:
            stat_line.write('Add\n')
            for date, value in add_log.items():
                for line in value[0]:
                    log_line.write(f'{line}\n')
                stat_line.write(f'{date} {value[1]}\n')
            

def main():
    write_logs()

if __name__=="__main__":
    main()










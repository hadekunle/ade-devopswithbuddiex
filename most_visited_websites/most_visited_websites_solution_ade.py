
from os import path, system
from pprint import pprint
from sys import argv as argument

system('clear')

def top_sites(log_file):
    websites_dict={}
    with open (log_file,'r') as file:
        for line in file: 
            parts = line.strip().split()[1:]

            for website in parts:
                if website not in websites_dict:
                    websites_dict[website] = 1
                else:
                    websites_dict[website]+= 1

    sorted_sites = sorted(websites_dict.items(), key=lambda kv: (kv[1]),reverse=True)
    return sorted_sites[:5]


def main():
    if len(argument) > 2:
        error_message="\nDon't forget to pass in the log file ONLY"
        raise ValueError(f"{error_message}")
    elif len(argument) == 2 :
        log_file = argument[1]
    else:
        log_file = 'file'

    if not path.exists(log_file):
        raise FileNotFoundError(f"{log_file} does not exist")

    pprint(top_sites(log_file))

        
if __name__ == "__main__":
    main()
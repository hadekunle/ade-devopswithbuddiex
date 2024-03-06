from os import path, system
from sys import argv as argument

system('clear') # Don't worry abourrit 

def remove_dup(filename: str):
    with open(filename,'r') as file:
        return list(set(file))

def write_unique(filename: str):
    with open('dedup_report_ade','w') as file:
        for each in remove_dup(filename):
            file.write(each)

def main():
    if len(argument) == 1:
        input_a='file'
    elif len(argument) == 2:
        input_a = argument[1]  #This should be the filename
    else:
        error_message="...\n\nDon't forget to pass in the filename only\n"
        raise ValueError(f"{error_message}")
    
    if not path.exists(input_a):
        raise FileNotFoundError(f"...\n\n{input_a} does not exist\n")
    
    write_unique(input_a)

if __name__ == '__main__' :
    main()

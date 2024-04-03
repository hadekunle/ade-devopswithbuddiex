import sys

def dedup_file(input_file, new_file_path):
    ''' This function takes an input file and removes duplicate'''
    ordered_list = []
    with open(input_file, 'r') as input:
        for line in input:
            line = line.strip()
            if line not in ordered_list:
                ordered_list.append(line)
    with open(new_file_path, 'w') as output:
        for line in ordered_list:
            output.write(line + '\n')
    return 

def main():
    '''main function'''
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        new_file_path = sys.argv[2]
        dedup_file(input_file, new_file_path)
    else:
        print("Invalid format, expected an input file and a output file: main.py input_file new_file_name ")

if __name__ == "__main__":
    main()
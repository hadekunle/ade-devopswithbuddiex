import sys

def create_usernames(input_file):
    ''' This function takes an input file and extracts the usernames'''
    records = {}
    with open(input_file, 'r') as input:
        #read the header in the file 
        header = input.readline()
        header = header.strip()
        header += " Username\n"
        for line in input:
            line = line.strip()
            firstname, lastname, employeeID, startDate = line.split()
            username = firstname[0] + lastname
            username = username.lower()
            if username not in records:
                records[username] = [line, 1]
            else:
                current_count = records[username][1]
                next_count = current_count + 1 
                records[username][1] = next_count
                username = firstname[0] + lastname + str(next_count)
                username = username.lower()
                records[username] = [line]
    return records, header

def write_file(input_file, new_file_path):
    '''function to write to an output file'''
    records, header = create_usernames(input_file)
    with open(new_file_path, 'w') as output:
        output.write(header)
        for username, line in records.items():
            full_line = line[0] + ' ' + username + '\n'
            output.write(full_line)
    return

def main():
    '''main function'''
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        new_file_path = sys.argv[2]
        write_file(input_file, new_file_path)
    else:
        print("Invalid format, expected an input file and a output file: main.py file new_file_name ")

if __name__ == "__main__":
    main()
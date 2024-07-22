import sys 

from datetime import datetime

def sort_function(input_file, column=2):
    output = []
    dict_out = {}
    with open(input_file, 'r') as lines:
        for line in lines:
            line = line.strip()
            name, date, number = line.split()
            date = datetime.strptime(date, "%m/%d")
            number = int(number)
            output.append((name, date, number))
            dict_out[(name, date, number)] = line
    try:
        output = sorted(output, key=lambda x: x[column])
    except IndexError:
        print("provide column, 0, 1 or 2")
        return
    for line in output:
        print(dict_out[line])
            

def main():
    input = sys.argv[1]
    column_input = sys.argv[2]
    try:
        column_input = int(column_input)
        sort_function(input, column_input)
    except IndexError:
        print("provide column, 0, 1 or 2")
    except ValueError:
        print("provide a numeric value")
    
    

if __name__ == "__main__":
    main()



import sys

def last_n_lines(input_file, n=10):
    line_list = []
    with open(input_file, 'r') as lines:
        for line in lines:
            if line != '\n':
                line_list.append(line)
        
        tail = line_list[-n:]
        for line in tail:
            print(line)

def main():
    input_file = sys.argv[1]
    n = input("Provide a number N \n")
    print('\n')
    try:
        last_n_lines(input_file, int(n))
    except:
        print("Invalid input")

if __name__ == "__main__":
    main()
import sys
import re

def valid_emails(input_file):
    pattern = r'^[A-Za-z0-9]+(-[A-Za-z0-9]+)*@[A-Za-z]+\.(com|net|edu|gov)$'

    with open(input_file, 'r') as lines:
        for line in lines:
            line = line.strip().split()
            email = line[2]
            if re.match(pattern, email):
                print(email)
    return



def main():
    file = sys.argv[1]
    valid_emails(file)


if __name__ == "__main__":
    main()
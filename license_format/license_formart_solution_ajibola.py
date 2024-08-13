import sys
import re 


def license(file):
    pattern = r'^[1-9][A-HJ-NP-Z]{3}(?!000|111|222|333|444|555|666|777|888|999)[0-9]{3}$'
    with open(file, 'r') as lines:
        for line in lines:
            line = line.strip()
            if re.match(pattern, line):
                print(f'This is a valid license: {line}')
            else:
                print(f'This is not a valid license: {line}')

def main():
    file = sys.argv[1]
    license(file)

if __name__ == "__main__":
    main()
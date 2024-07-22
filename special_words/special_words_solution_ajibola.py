import sys
import re

def special_words(input_file):
    pattern = r'(?i)^her\w*|^he\w*er\w*'
    with open(input_file, 'r') as lines:
        for line in lines:
            if re.match(pattern, line):
                print(line)



def main():
    file = sys.argv[1]
    special_words(file)

if __name__ == "__main__":
    main()
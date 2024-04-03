import sys
import re

def find_phone(file):
    patterns = ["^[0-9]{3}-[0-9]{3}-[0-9]{4}$", "^[0-9]{3}\\.[0-9]{3}\\.[0-9]{4}$", "^[0-9]{3} [0-9]{3} [0-9]{4}$", "^\\([0-9]{3}\\) [0-9]{3} [0-9]{4}$", "^\\([0-9]{3}\\) [0-9]{3}-[0-9]{4}$"]
    with open(file, 'r') as fp:
        for line in fp:
            line = line.strip().split()
            name = line[0:2]
            name = " ".join(name)
            phone_number = line[2:]
            phone_number = " ".join(phone_number)

            for pattern in patterns:
                match = re.search(pattern, phone_number)
                if match:
                    print(name, match.group(0))
                    break


def main():
    file = sys.argv[1]
    find_phone(file)

if __name__ == "__main__":
    main()
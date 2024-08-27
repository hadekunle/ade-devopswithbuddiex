import sys
from datetime import datetime

def sort_file(input_file):
    file = []
    with open(input_file, 'r') as lines:
        for line in lines:
            parts = line.strip().split()
            date = " ".join(parts[2:5])
            name = parts[5]
            clean_date = datetime.strptime(date, '%B %d, %Y')
            file.append((name, clean_date))
    file = sorted(file, key = lambda x:x[1], reverse=True)
    for value in file:
        date = value[1].strftime("%B %d, %Y")
        print(f'{value[0]}, {date}')

def main():
    input_file = sys.argv[1]
    sort_file(input_file)

if __name__ == "__main__":
    main()
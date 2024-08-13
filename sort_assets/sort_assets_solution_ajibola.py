import sys
from datetime import datetime

def sort_assets(file):
    output_list = []
    serial = 0
    with open(file, 'r') as lines:
        next(lines)
        for line in lines:
            model, date, assignee = line.strip().split()
            date = datetime.strptime(date, '%m/%d/%Y')
            output_list.append([model, date, assignee])
    output_list = sorted(output_list, key=lambda x: (x[0], x[1]))
    for value in output_list:
        serial += 1
        asset_number = str(serial).rjust(6, '0')
        date = value[1].strftime('%m/%d/%Y')
        value[1] = date
        value.insert(0, asset_number)
        print(" ".join(value))

def main():
    file = sys.argv[1]
    sort_assets(file)

if __name__ == "__main__":
    main()
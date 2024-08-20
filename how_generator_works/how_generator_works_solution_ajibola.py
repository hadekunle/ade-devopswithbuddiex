import sys

def generator(input_file):
    total = 0
    count = 0 
    with open(input_file, 'r') as lines:
        for line in lines:
            line = line.strip('\n')
            if line.isnumeric():
                total += float(line)
                count += 1
    average = total / count
    print(f"The average of the numbers is: {average}")
    print(f"The Sum is: {total} and Count is: {count}")


def main():
    input_file = sys.argv[1]
    generator(input_file)

if __name__ == "__main__":
    main()
import sys

def print_median(input_file): 
    output_list = []
    count = 0
    with open(input_file, 'r') as lines:
        for line in lines:
            line = line.strip()
            output_list.append(line)
            count += 1
        median = count/2
        if count % 2 == 0:
            print(output_list[int(median) - 1 ])
            print(output_list[int(median)])
        else:
            print(output_list[round(median)])
        print(output_list)

def main():
    input_file = sys.argv[1]
    print_median(input_file)

if __name__ == "__main__":
    main()
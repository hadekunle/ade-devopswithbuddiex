import sys

def group_name(input_file):
    output = []
    with open(input_file, 'r') as lines:
        for line in lines:
            line = line.strip().split()
            output.append(line)
    return output

def write_to_file(output_list):
    output_list_sorted = sorted(output_list, key=lambda x: x[1])
    with open("aji_test_file", "w") as lines:
        for line in output_list_sorted:
            lines.write(" ".join(line) + "\n")
    return 

def main():
    input_file = sys.argv[1]
    output_list = group_name(input_file)
    write_to_file(output_list)


if __name__ == "__main__":
    main()
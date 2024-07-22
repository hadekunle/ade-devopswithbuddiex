import sys 
import re

def write_file(output):
    with open("new_aji_file", 'w') as file:
        for line in output:
            file.write(line + "\n")
    return 
    

def standard_ip(input_file):
    pattern = r'^((0|[1-9]\d{0,2})\.){3}(0|[1-9]\d{0,2})$'
    output = []
    with open(input_file, 'r') as lines:
        for line in lines:
            line = line.strip()
            if re.match(pattern, line):
                output.append(line)
            else:
                line = re.sub(r'[^\d.]+', '.', line)
                line = re.sub(r'\b0+(\d)', r'\1', line)
                output.append(line)
    write_file(output)


def main():
    file = sys.argv[1]
    standard_ip(file)


if __name__ == "__main__":
    main()
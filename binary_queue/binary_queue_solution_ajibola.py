import sys

def read_queue(file):
    """A function that acepts a file of different binaries and their status, removes completed binary and sorts the queue and running binaries."""
    output_list = []
    with open (file, 'r') as binary:
        header = binary.readline()
        for line in binary:
            line = line.strip()
            status = line.split()[3]
            if status.lower() != 'succeeded' and status.lower() != 'failed':
                output_list.append(line)
    
    #sort output_list
    output_list.sort(key=lambda x: (x.split()[3], x.split()[1]))

    return (header, output_list)

def write_queue(input_file, destination_file):
    header, output = read_queue(input_file)
    with open(destination_file, 'w') as binary:
        binary.write(header)
        for line in output:
            binary.write(line + "\n")
    return 





def main():
    binary_file = sys.argv[1]
    destination_file = sys.argv[2]
    if len(sys.argv) != 3:
        sys.exit("please provide an input and a destination file")
    write_queue(binary_file, destination_file)

if __name__ == "__main__":
    main()
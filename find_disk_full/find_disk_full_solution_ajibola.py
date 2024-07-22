import sys 

def disk_full(input_file):
    with open(input_file, 'r') as lines:
        for line in lines:
            server, _, _, usage = line.strip().split()
            usage_strip = float (usage[:-1])
            if usage_strip > 85:
                print(server, usage)
    return 

def main():
    input_file = sys.argv[1]
    disk_full(input_file)


if __name__ == "__main__":
    main()
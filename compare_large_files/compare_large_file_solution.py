import sys

def compare_file(file1, file2):
    file1_list = []
    file2_list = []
    with open(file1, 'r') as lines1, open(file2, 'r') as lines2:
        for line in lines1:
            line = line.strip()
            file1_list.append(line)
        for line in lines2:
            line = line.strip()
            file2_list.append(line)
    file1_list.sort()
    file2_list.sort()

    print(file1_list == file2_list)

def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    compare_file(file1, file2)

if __name__ == "__main__":
    main()
import sys 





def dedup_file(file):
    remove_duplicates = []
    with open(file, 'r') as f:
        for line in f:
            if line in remove_duplicates:
                continue
            else:
                remove_duplicates.append(line)
    return remove_duplicates


def output(data):
    with open("new_file", "w") as f:
        for line in data:
            f.write(line)



def main():
    output(dedup_file(sys.argv[1]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dedup_file_solution_eloho.py <file>")
        sys.exit(1)
    else:
        print("File deduplicated!!!")
        main()
        sys.exit(0)
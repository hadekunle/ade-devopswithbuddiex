import sys


def read_file(filename):
    data = {}
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                data[parts[0]] = parts[1]
            else:
                print(f"Error: Line '{line.strip()}' in file '{filename}' has fewer elements than expected.")
    return data


def format_output(fileA_data, fileB_data):
    output = []
    for username, status in fileB_data.items():
        if status.lower() == "yes":
            email = username.split('@')[1]
            if email.startswith('yaboo'):
                if username in fileA_data:
                    output.append(f"{username} ({fileA_data[username]})")
                else:
                    output.append(f"{username} (444) 123-1233")
    return output


def main(fileA, fileB):
    fileA_data = read_file(fileA)
    fileB_data = read_file(fileB)
    output = format_output(fileA_data, fileB_data)
    for line in output:
        print(line)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python active_users_finder.py fileA fileB")
        sys.exit(1)
    fileA = sys.argv[1]
    fileB = sys.argv[2]
    main(fileA, fileB)

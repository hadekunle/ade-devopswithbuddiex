import sys
import re


def read_messed_up_file(filename):
    """Reads the content of the file and returns a list of lines."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)


def messed_up_file_split(lines):
    results = []
    # Define regular expression pattern
    pattern = r'(?:(?P<Username>[A-Za-z]+)|(?P<Phone_num>\d{3}-\d{3}-\d{4})|(?P<Start_date>\d{2}/\d{2}/\d{4}))'
    # Iterate over the lines
    for line in lines:
        # Find all matches in the line
        matches = re.finditer(pattern, line)

        # Create a dictionary to store the matched groups
        match_dict = {}
        # Store the matched groups in the dictionary
        for match in matches:
            for key, value in match.groupdict().items():
                if value:
                    match_dict[key] = value

        # Append the dictionary to the results list
        results.append(match_dict)
    return results


def create_file_with_format(filename):
    lines = read_messed_up_file(filename)
    data = messed_up_file_split(lines)
    # Sort the data by name
    sorted_data = sorted(data, key=lambda x: x.get('Username', ''))

    # Write the sorted data to the file
    with open('result_file', 'w') as file:
        file.write("Username Phone_num Start_date\n")
        for entry in sorted_data:
            file.write(f"{entry.get('Username', '')} {entry.get('Phone_num', '')} {entry.get('Start_date', '')}\n")


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file>")
        sys.exit(1)
    filename = sys.argv[1]
    create_file_with_format(filename)


if __name__ == "__main__":
    main()

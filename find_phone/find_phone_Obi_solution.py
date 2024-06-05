from pprint import pprint
def extract_valid_us_phone_numbers(file_path):
    import re
    phone_number_pattern = re.compile(
        r"""
        \(?          # optional opening parenthesis
        \d{3}        # area code
        \)?          # optional closing parenthesis
        [\s.-]?      # optional separator (space, dot, or dash)
        \d{3}        # first 3 digits
        [\s.-]?      # optional separator (space, dot, or dash)
        \d{4}        # last 4 digits
        """, re.VERBOSE)
    
    valid_numbers = []  # List to store valid phone numbers

    with open(file_path, 'r') as file:
        for line in file:
            possible_numbers = phone_number_pattern.findall(line)
            valid_numbers.extend(possible_numbers)

    return valid_numbers





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py log_file")
        sys.exit(1)
    
    file = sys.argv[1]
    valid_numbers = extract_valid_us_phone_numbers(file)
    pprint(valid_numbers)
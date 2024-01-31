import sys


# First I will create a function that extracts the username and phone number from the first file
def extract_username_and_number(file):
    company_number = "(444) 123-1233"
    data = {}
    with open(file, 'r') as f:
        for line in f:
            fields = line.strip()
            # split the line by @ to get the username
            username = fields.split('@')[0]
            email = fields.split(' ')[0]
            # since there are two spaces between the email and the phone number, I will split by space and get the last two items
            try:
                # if there is no phone number in the line, I will use the company number
                area_code, suffix = fields.split(' ')[-2:]
                phone_number = f'{area_code} {suffix}'
            except ValueError:
                phone_number = company_number
            data[username] = { 'email': email, 'phone_number': phone_number}
    return data

# Next I will create a function that saves the username and is_active status from the second file
def is_active_user(file):
    data = {}
    with open(file, 'r') as f:
        next(f)
        for line in f:
            fields = line.strip()
            username = fields.split(' ')[0]
            is_active = fields.split(' ')[-1]
            data[username] = { 'is_active': is_active}
        
            
    return data



def main():
    if len(sys.argv) != 3:
        print("Usage: python active_user_solution_eloho.py <file1> <file2>")
        sys.exit(1)
        
# I will take in the two files as arguments
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    data1 = extract_username_and_number(file1)
    data2 = is_active_user(file2)

# I will loop through the first file and check if the username is in the second file and if the user is active
    for username, info in data1.items():
        if username in data2 and data2[username]['is_active'] == 'Yes':
            print(f"{username} {info['phone_number']}")
        

if __name__ == '__main__':
    main()
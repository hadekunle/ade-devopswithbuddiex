import sys
import os
import re

def process_and_sort_contacts(file, f):
    # Regular expression patterns to identify phone numbers and dates
    phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    date_pattern = re.compile(r'\d{2}/\d{2}/\d{4}')
    
    contacts = []
    
    with open(file, 'r') as file:
        for line in file:
            phone_match = phone_pattern.search(line)
            date_match = date_pattern.search(line)
            if phone_match and date_match:
                phone_num = phone_match.group()
                start_date = date_match.group()
                # Remove the identified phone number and date from the line
                name_part = phone_pattern.sub('', line)
                name_part = date_pattern.sub('', name_part)
                # Clean up to get the name
                username = re.sub(r'[^a-zA-Z]+', '', name_part)
                contacts.append((username, phone_num, start_date))
    
    # Sort contacts by username
    sorted_contacts = sorted(contacts, key=lambda x: x[0])
    
    # Write the sorted contacts to the output file
    with open(f, 'w') as file:
        file.write("Username Phone_num Start_date\n")
        for username, phone_num, start_date in sorted_contacts:
            file.write(f"{username} {phone_num} {start_date}\n")



if __name__ == "__main__":
    debug = True
    # if len(sys.argv) != 2:
    #     print("We the the messy file")
    #     sys.exit(1)
    # else:
    #     file = sys.argv[1]
    #     cwd = os.getcwd()
    #     path_b = cwd + "result.txt"
    #     print(cwd)
        process_and_sort_contacts(file, path_b)
  
    
        
         


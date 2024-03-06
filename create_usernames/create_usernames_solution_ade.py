from os import path, system
from sys import argv as argument

system('clear')

def main(filename,report_name):
    used_usernames =[]
    
    with open(report_name,'w') as file:
        header= 'Firstname | Lastname | EmpID |   StartDate   | Username\n'
        file.write(header)         
        file.write(f"{'-'*56}\n")
    
    with open(filename,'r') as file:
        next(file)
        for line in file:
            new_uname = False
            first_name, last_name, employee_id, start_date = line.strip().split()
            username = first_name[0].lower() + last_name.lower()
            
            if username in used_usernames:
                counter = used_usernames.count(username)+1
                new_uname = f'{username}{counter}'
            used_usernames.append(username)
            
            if new_uname: username = new_uname

            with open(report_name,'a') as file:
                ad = 10
                file.write(f'{first_name.center(ad)}|{last_name.center(ad)}|{employee_id.center(ad-3)}|{start_date.center(ad+5)}|{username.center(ad)}\n')

if __name__ == '__main__' :
    if len(argument) == 1:
        input_a='file'
        input_b='report_ade'
    
    elif len(argument) == 3:
        input_a = argument[1]
        input_b = argument[2]
        if input_a == input_b:
            error_message="...\n\nDO NOT USE SAME NAME FOR FILE & REPORT \n"
            raise ValueError(f"{error_message}")

    else:
        error_message="...\n\nDon't forget to pass in the filename first, report name second\n"
        raise ValueError(f"{error_message}")
    
    if not path.exists(input_a):
        raise FileNotFoundError(f"...\n\n{input_a} does not exist\n")
    
    main(input_a,input_b)
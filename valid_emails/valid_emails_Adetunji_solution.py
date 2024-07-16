import os 
import re

folder =os.getcwd()
problem_file ="valid_emails/file"
#output_file= "valid_emails/newfile_Adetunji"
input_full_path = os.path.join(folder,problem_file)
#output_file_path=os.path.join(folder,output_file)

pattern =r'^[a-zA-Z0-9][a-zA-Z0-9-]+@[a-zA-Z]+\.(com|net|edu|gov)$'
counts=0
with open(input_full_path,"r") as file:
    for x in file:
        email_address = x.split(" ")[2]
        if re.match(pattern,email_address):
            counts= counts +1
            print(email_address)
        else:
            pass
    print(f"Total count is :", {counts})
    
#pattern =^[a-zA-Z0-9][a-zA-Z0-9-]+@[a-zA-Z]+\.(com|net|edu|gov)$
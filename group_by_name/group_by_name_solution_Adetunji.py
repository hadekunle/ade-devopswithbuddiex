import os 
import re

folder =os.getcwd()
problem_file ="group_by_name/file1"
output_file= "group_by_name/newfile_Adetunji"
input_full_path = os.path.join(folder,problem_file)
output_file_path=os.path.join(folder,output_file)
sort_column = 1


def group_by_name(input_full_path,output_file_path):
    
    with open(input_full_path,"r") as file:
        lines = file.readlines()
        parsed_line = [line.split() for line in lines]
        sorted_lines_by_column = sorted(parsed_line, key =lambda x: x[sort_column])
        sorted_lines=[' '.join(line) for line in sorted_lines_by_column]
        #print(parsed_line)
        
    with open(output_file_path,"w") as doc:
        for line in sorted_lines:
            doc.write(line +'\n')
        
group_by_name(input_full_path,output_file_path)
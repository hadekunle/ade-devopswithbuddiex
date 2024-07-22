import os
def sort_by_groupname(input_file, output_file):
    with open(input_file, "r") as file:
        lines = file.readlines()


    lines = [line.strip() for line in lines]

   
    sorted_lines = sorted(lines, key=lambda x: x.split()[1])

    with open(output_file, "w") as file:
        for line in sorted_lines:
            file.write(line + "\n")

def sort_by_groupname(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines]
    
    sorted_lines = sorted(lines, key=lambda x: x.split()[1])
    
    with open(output_file, 'w') as file:
        for line in sorted_lines:
            file.write(line + '\n')



if __name__ == "__main__":
    dir_a = "group_by_name/newfile2"
    dir_b ="group_by_name/newfile2_soln"
    soln(directory_path)
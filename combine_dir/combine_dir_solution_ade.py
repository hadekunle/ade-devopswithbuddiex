import os
import shutil
from sys import argv as argument

os.system('clear')

def list_files(directory,new_directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        root_new = root.replace(directory,new_directory)
        os.makedirs(root_new, exist_ok=True)

        for file in files:
            full_path = os.path.join(root, file)
            all_files.append(full_path.lstrip(directory))
    return all_files

def process_merge(directory_1,directory_2):
    # directory_1 = './dir1'
    # directory_2 = './dir2'
    new_directory = './new_dir_ade'



    list_dir_2 = list_files(directory_2,new_directory)
    list_dir_1 = list_files(directory_1,new_directory)

    for i in list_dir_2:
        if i in list_dir_1:
            src_0, target_0  = f'{directory_2}/{i}', f'{new_directory}/{i}'
            src_1, target_1 = f'{directory_1}/{i}', f'{new_directory}/{i}_2'
            
            shutil.copy(src_0, target_0)
            shutil.copy(src_1, target_1)
            
            list_dir_1.remove(i)
        else:
            src_2, target_2  = f'{directory_2}/{i}',f'{new_directory}/{i}'
            shutil.copy(src_2, target_2)

    for i in list_dir_1:
        src_3, target_3 = f'{directory_1}/{i}', f'{new_directory}/{i}'
        shutil.copy(src_3, target_3)

def main():
    if len(argument) != 3:
        error_message="\nDon't forget to pass in two dirs"
        raise ValueError(f"{error_message}")

    input_a = argument[1] #This should be the main Dir, './dir2'
    input_b = argument[2] #This should be the branch Dir being merged, './dir1'

    process_merge(directory_1=input_a,directory_2=input_b)

if __name__ == "__main__":
    main()
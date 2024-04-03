import os 
import sys
import shutil



def combine_dir(dir1, dir2, new_dir):
    #check if new_dir exists
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # Iterate through the first directory and copy the contents to the new directory
    for root, dirs, files in os.walk(dir1):
        rel_path = os.path.relpath(root, dir1)
        new_rel_path = os.path.join(new_dir, rel_path)

        # create subdirs in new_dir
        if not os.path.exists(new_rel_path):
            os.makedirs(new_rel_path)

        # copy files from dir1 to new_dir
        for file in files:
            old_file = os.path.join(root, file)
            new_file = os.path.join(new_rel_path, file)
            shutil.copy(old_file, new_file)


    # Iterate through the second directory and copy the contents to the new directory

    for root, dirs, files in os.walk(dir2):
        rel_path = os.path.relpath(root, dir2)
        new_rel_path = os.path.join(new_dir, rel_path)

        # create subdirs in new_dir
        if not os.path.exists(new_rel_path):
            os.makedirs(new_rel_path)

        # copy files from dir2 to new_dir
        for file in files:
            old_file = os.path.join(root, file)
            new_file = os.path.join(new_rel_path, file)

            # check if file exists in new_dir
            counter = 2
            while os.path.exists(new_file):
                base, ext = os.path.splitext(file)
                new_file = os.path.join(new_rel_path, base + f"_{counter}" + ext)
                counter += 1
            shutil.copy(old_file, new_file)
    




if __name__ == "__main__":
    if len(sys.argv) == 4:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
        new_dir = sys.argv[3]
        combine_dir(dir1, dir2, new_dir)
        #remove the first directory
        print(f"Removing {dir1}")
        shutil.rmtree(dir1)
        #remove the second directory
        print(f"Removing {dir2}")
        shutil.rmtree(dir2)
        print("Files have been combined successfully")
    else:
        print("Usage: python combine_dir_solution_eloho.py dir1 dir2 new_dir")
        sys.exit(1)
    
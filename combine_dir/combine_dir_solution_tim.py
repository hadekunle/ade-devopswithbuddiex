import os


def copy_file(src_file, dest_file):
    dest_dir = os.path.dirname(dest_file)
    os.makedirs(dest_dir, exist_ok=True)
    with open(src_file, 'rb') as src, open(dest_file, 'wb') as dest:
        dest.write(src.read())


def combine_directories(dir1_backup, dir2_backup, new_dir_tim):
    # Create the new directory
    os.makedirs(new_dir_tim, exist_ok=True)

    # Copy files from dir1_backup to new_dir_
    for root, _, files in os.walk(dir1_backup):
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(new_dir_tim, os.path.relpath(src_file, dir1_backup))
            copy_file(src_file, dest_file)

    # Copy files from dir2_backup to new_dir_
    for root, _, files in os.walk(dir2_backup):
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(new_dir_tim, os.path.relpath(src_file, dir2_backup))
            if not os.path.exists(dest_file):
                copy_file(src_file, dest_file)

    # Remove dir1_backup and dir2_backup if they are empty
    if os.path.isdir(dir1_backup) and not os.listdir(dir1_backup):
        os.rmdir(dir1_backup)
    else:
        print(f"{dir1_backup} is not empty or is not a directory, skipping deletion.")
    if os.path.isdir(dir2_backup) and not os.listdir(dir2_backup):
        os.rmdir(dir2_backup)
    else:
        print(f"{dir2_backup} is not empty or is not a directory, skipping deletion.")


def main():
    dir1_backup = 'dir1_backup'
    dir2_backup = 'dir2_backup'
    new_dir_tim = 'new_dir_tim'
    combine_directories(dir1_backup, dir2_backup, new_dir_tim)


if __name__ == "__main__":
    main()

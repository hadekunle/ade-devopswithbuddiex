import sys
import os

def small_files(input_directory="./test_dir_backup/"):
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            full_path = os.path.join(root, file)
            #3000bytes = 3KB
            if os.path.getsize(full_path) < 3000:
                os.remove(full_path)
                print(f"removed {full_path}")

    return 


def main():
    small_files()

if __name__ == "__main__":
    main()
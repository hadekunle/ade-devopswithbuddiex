import os

def list_and_remove_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path) / 1024  # size in KB
            print(f"{file} {file_size:.1f}KB")
            if file_size < 3:
                os.remove(file_path)
                print(f"{file} removed!")


if __name__ == "__main__":
    # Directory name
    directory_name = 'remove_small_files/test_dir'

    # Call the function
    list_and_remove_files(directory_name)

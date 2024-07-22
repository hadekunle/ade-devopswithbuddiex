# import os
# import shutil


# def organize_files(directory):
#     # Create a directory named 'pictures' if it doesn't exist
#     pictures_dir = os.path.join(directory, 'pictures')
#     os.makedirs(pictures_dir, exist_ok=True)

#     # Iterate over files in the directory
#     for filename in os.listdir(directory):
#         filepath = os.path.join(directory, filename)
#         if os.path.isfile(filepath):
#             # Move .jpg 
#             if filename.endswith('.jpg'):
#                 shutil.move(filepath, os.path.join(pictures_dir, filename))
#             # Rename .html 
#             elif filename.endswith('.html'):
#                 new_filename = os.path.splitext(filename)[0] + '.htm'
#                 os.rename(filepath, os.path.join(directory, new_filename))

#     # Concatenate and sort all .txt 
#     txt_files = [filename for filename in os.listdir(directory) if filename.endswith('.txt')]
#     txt_files.sort()
#     with open(os.path.join(directory, 'stuff.txt'), 'w') as outfile:
#         for txt_file in txt_files:
#             with open(os.path.join(directory, txt_file), 'r') as infile:
#                 outfile.write(infile.read())

import os
import shutil

def organize_files(directory):
    # Create a directory named 'pictures' if it doesn't exist
    pictures_dir = os.path.join(directory, 'pictures')
    os.makedirs(pictures_dir, exist_ok=True)

    # Initialize a list to store the content of all text files
    text_content = []

    # Iterate over all files and directories in the given directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # If it's a file
        if os.path.isfile(item_path):
            # If it's a JPG file, move it to the 'pictures' directory
            if item.endswith('.jpg'):
                shutil.move(item_path, os.path.join(pictures_dir, item))
            # If it's an HTML file, rename it to .htm
            elif item.endswith('.html'):
                os.rename(item_path, os.path.join(directory, os.path.splitext(item)[0] + '.htm'))
            # If it's a text file, append its content to the list
            elif item.endswith('.txt'):
                with open(item_path, 'r') as file:
                    text_content.append(file.read())
        # If it's a directory, recursively call organize_files on it
        elif os.path.isdir(item_path):
            organize_files(item_path)

    # Sort the text content alphabetically
    text_content.sort()

    # Write the sorted text content to a file named 'stuff.txt'
    with open(os.path.join(directory, 'stuff.txt'), 'w') as outfile:
        for content in text_content:
            outfile.write(content)





if __name__ == "__main__":
   directory_path = 'file_manipulation'
   organize_files(directory_path)

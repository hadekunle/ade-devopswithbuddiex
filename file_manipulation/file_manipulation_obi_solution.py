import os
import shutil


def organize_files(directory):
    # Create a directory named 'pictures' if it doesn't exist
    pictures_dir = os.path.join(directory, 'pictures')
    os.makedirs(pictures_dir, exist_ok=True)

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Move .jpg 
            if filename.endswith('.jpg'):
                shutil.move(filepath, os.path.join(pictures_dir, filename))
            # Rename .html 
            elif filename.endswith('.html'):
                new_filename = os.path.splitext(filename)[0] + '.htm'
                os.rename(filepath, os.path.join(directory, new_filename))

    # Concatenate and sort all .txt 
    txt_files = [filename for filename in os.listdir(directory) if filename.endswith('.txt')]
    txt_files.sort()
    with open(os.path.join(directory, 'stuff.txt'), 'w') as outfile:
        for txt_file in txt_files:
            with open(os.path.join(directory, txt_file), 'r') as infile:
                outfile.write(infile.read())



if __name__ == "__main__":
   directory_path = 'file_manipulation'
   organize_files(directory_path)

import os
import shutil

base_directory = os.path.dirname(os.path.abspath(__file__))
curr_dir = f'{base_directory}/backup'
target  = f'{base_directory}/backup2'
os.makedirs(f'{target}/pictures/', exist_ok=True)

def list_files(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            all_files.append(file)
    return all_files

list_dir_1 = list_files(curr_dir)

all_txt=[]
for each in list_dir_1:
    if each.endswith('.jpg'):
        src_1 = f'{curr_dir}/{each}'
        target_1 = f'{target}/pictures/{each}'
        shutil.copy(src_1, target_1)

    elif each.endswith('.html'):
        src_1 = f"{curr_dir}/{each}"
        target_1 = f"{target}/{each.replace('.html','.htm')}"
        shutil.copy(src_1, target_1)

    elif each.endswith('.txt'):
        all_txt.append(each)

combined_txt = "stuff.txt"
all_txt = sorted(all_txt)
for each in all_txt:
    if each != 'stuff.txt':
        os.system(f'cat {curr_dir}/{each} >> {target}/{combined_txt}')
import os

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/test_dir_backup2'

def list_files(path):
    files_to_del=[]
    for root, dirs, files in os.walk(path):
        print(root.split('/')[-1]+'/')
        for file in files:  
            #use "command [" to indent left
            #use "command ]" to indent right
            full_path = os.path.join(root, file)
            file_size = os.path.getsize(full_path) / 1024
            print(f'{file} {file_size:.1f}KB')

            if file_size < 3:
                files_to_del.append(full_path)

    if files_to_del:    
        print()
        print([os.path.basename(each) for each in files_to_del])
        
        check = input('\nDo you want to delete these files listed above: Y/N ? ')
        if check.lower() == 'y':
            print()
            for each in files_to_del:
                os.remove(each)
                print(os.path.basename(each),'removed!')
        else:
            print('\nFile deletion not approved\n')


list_files(path)



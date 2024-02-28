import os

# print(os.name)
# print(os.getenv(key='HOME',default='not_avail'))
# print(os.listdir('.'))

files=os.walk('.')

#Shows up as a tuple
#   (dirpath, dirnames, filenames)

path1='./dir1_backup'
for root, dirs, files in files:
    print(root,files)

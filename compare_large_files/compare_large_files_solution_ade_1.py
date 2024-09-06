import os

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))

with open(f'{directory}/file1','r') as fileA:
    contentA = fileA.readlines()

with open(f'{directory}/file2','r') as fileB:
    contentB = fileB.readlines()

for i in range(max(len(contentA),len(contentB))):
    if contentA[i] == contentB[i]:
        pass
        # print(f'Line {i+1} has the same content')
    else:
        print(f'Line {i+1} has different content')
        exit()
print('Both files are the same')
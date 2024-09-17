import os

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))

def fileA_content():
    count = 0
    with open(f'{directory}/file1','r') as fileA:
        for lineA in fileA:
            count += 1
            yield count,lineA.strip()

def fileB_content():
    count = 0
    with open(f'{directory}/file2','r') as fileB:
        for lineB in fileB:
            count += 1
            yield count,lineB.strip()

def compare(fileA,fileB):
    while True:
        try:
            lineA_num, lineA_content = next(fileA)
        except StopIteration:
            try:
                lineB_num, lineB_content = next(fileB)
                print(f"File B is longer than File A, starting from line {lineB_num}.")
                return False
            except StopIteration:
                return True

        try:
            lineB_num, lineB_content = next(fileB)
        except StopIteration:
            print(f"File A is longer than File B, starting from line {lineA_num}.")
            return False

        if lineA_content != lineB_content:
            print(f'The contents are different on line {lineA_num}.')
            return False

print(compare(fileA_content(),fileB_content()))
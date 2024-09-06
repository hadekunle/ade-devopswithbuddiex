import os

os.system('clear')

directory = os.path.dirname(os.path.abspath(__file__))

def compare():
    try:
        count = 0
        with open(f'{directory}/file1', 'r', encoding='utf-8') as fileA, open(f'{directory}/file2', 'r', encoding='utf-8') as fileB:
            while True:
                count += 1

                lineA = fileA.readline()
                lineB = fileB.readline()

                if not lineA and not lineB:
                    return True
                
                lineA = lineA.strip()
                lineB = lineB.strip()

                if lineA != lineB:
                    print(f'The contents are different on line {count}.')
                    return False

    except Exception as e:
        print(f'Error: {e}')

print(compare())

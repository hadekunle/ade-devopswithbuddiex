import os
from statistics import median

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'
path2 = f'{directory}/ade_cleaned_file'

def clean_file():
    with open (path2,'w') as cleaned_file:
        with open (path,'r') as file:
            for line in file:
                if line.strip() != "":
                    cleaned_file.write(line)

def count_lines():
    with open (path2,'r') as file:
        counter = 0
        for line in file:
            counter += 1
            yield f'{counter}'

def is_float(med):
    if isinstance(med, float):
        med1,med2 = [int(med-0.5),int(med+0.5)]
        return [med1,med2]
    return [med]

def print_med(single_med,med,med1,med2):
    with open (path2,'r') as file:
        counter = 0
        for line in file:
            counter += 1
            if single_med:
                if counter == med:
                    yield f'{line.strip()}'
                elif counter > med:
                    break
            else:
                if counter == med1 or counter ==med2:
                    yield f'{line.strip()}'
                elif counter > med2:
                    break


def main():
    clean_file()
    lst = [int(i) for i in count_lines()]
    med = median(lst)
    floater = is_float(med)

    if len(floater) == 2:
        single_med = False
        med1,med2 = floater
    elif len(floater) == 1:
        single_med = True
        med = floater[0]
        med1,med2 = None, None

    with open (f'{directory}/ade_soln_file','w') as soln:
        mendy = [soln.write(f'{i}\n') for i in print_med(single_med,med,med1,med2)]

if __name__ == '__main__':
    main()
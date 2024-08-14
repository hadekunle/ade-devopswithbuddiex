import os

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/problem_statement'

def count_generator():
    with open (path,'r') as file:
        total   = 0
        counter = 0
        for line in file:
            try:
                total   += int(line.strip())
                counter += 1
            except:
                pass
            
            if counter==0:
                continue

            average = total/counter
            yield   f'{average:.2f}'

counter = count_generator()
overall_average = [i for i in counter]

if len(overall_average) > 0:
    print(f'Average of numbers in the file is {overall_average[-1]}')
else:
    print('File is empty')



















# def countdown_generator():
#     x = total
#     print(total)
#     counter = 0
#     total = 0
#     while x > 0:
#         yield 
#         x -= 1

# counter = countdown_generator()

# print(next(counter))
# print([i for i in counter])
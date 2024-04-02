import os

os.system('clear')

def compare(test_1 ,test_2 ):
    if len(test_1)>=len(test_2):
        return 'Same'
    if abs(len(test_1)-len(test_2)) >= 2:
        return False

    result = set(test_1)-set(test_2)
    return abs(len(result))<2

test_1="xyz"
for i in range(len(test_1)):
    test_1 = test_1
    char_list = list(test_1).pop(i)
    print(char_list)
    result = ''.join(char_list)
    print(result)


    
# print(compare())

# with open ('fileA.txt','r') as file:
#     counter = 0 
#     for line in file:
#         part= line.replace(' ','').strip().split(',')
#         print(compare(part[0],part[1]))
#         test_1 = part[0]
#         test_2 = part[1]
        # if len(test_2) > len(test_1):
        #     test_1, test_2 = test_2, test_1
        # counter += 1
        # print(f'This is for line {counter}')
        # print(f'{test_1=}\n{test_2=}')
        # print(compare(test_1,test_2))
        # print('\n')

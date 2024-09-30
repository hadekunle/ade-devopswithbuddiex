import os

os.system('reset')

def top_three(input):
    string = input + '-' 
    count, count_list = 1,[]
    for i in range(1,len(string)):
        if string[i]==string[i-1]:
            count += 1
        else:
            count_list.append((count, string[i-1]))
            count = 1
    count_list = sorted(count_list, key=lambda x: x[0], reverse=True )
    return count_list[:3] 

[ print(f'{i[1]},{i[0]}') for i in top_three('aaabbccadddeeee') ]
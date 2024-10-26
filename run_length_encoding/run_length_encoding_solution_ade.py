import os

os.system('reset')

input = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
input = input + '-'
output='12W1B12W3B24W1B14W'

count, count_list = 1, []
for i in range(1, len(input)):
    if input[i] == input[i-1]:
        count += 1
    else:
        count_list.append((count, input[i-1]))
        count = 1
count_list = [str(x[0])+x[1] for x in count_list]
count_list = ''.join(count_list)
print(count_list==output)
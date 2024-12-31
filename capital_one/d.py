example = [1,2,3,4,7,5,3,4,5,6,7]
example = [1,2,3,4,2,3,4,5,6,7,8]

count = 1
longest = 0
for i in range(1,len(example)):
    if example[i] > example[i-1]:
        count += 1
    else:
        longest = max(longest,count)
        count = 1
longest = max(longest,count)

print(longest)
import os

os.system('clear')

def solution(numbers):
    # unique = []
    count = 0
    for x in numbers:
        for y in numbers:
            diff_count = 0
            a = str(x)
            b = str(y)
            if len(a) != len(b) or a==b:
                continue
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff_count += 1
                    if diff_count > 1:
                        break
            if diff_count == 1:
                count += 1
                # unique.append([a,b])
    # print(*unique,sep='\n')
    return int(count/2)

print(solution([1, 151, 241, 1, 9, 22, 351]))
print(solution([1,2]))
print(solution([1,1,1,1,1,1]))


def mix(arr):
    for i in range(0,len(arr)-1,2):
        if arr[i] > arr[i+1] :
            arr[i] , arr[i+1] = arr[i+1],arr[i]
    return arr

print(mix([1, 5, 7, 3, 2, 1]))
print(mix([6, 7, 8, 8, 5, 3, 2]))
print(mix([9,8,7,6]))
def list_sort(lst):
    def sorting_key(item):
        letter = item[0]      
        number = int(item[1:])  
        return (letter, number)

    lst.sort(key=sorting_key)
    return lst

input_list = ['a1', 'b2', 'c1', 'd5', 'a3', 'b1', 'd1', 'b3']

sorted_list = list_sort(input_list)

print(sorted_list)

# You are given two lists, please do the following:
# 1) write a function named xor_lists to combine two lists with items in either list but not both.
# example:
# a = [1, 2, 3]
# b = [2, 4, 6]
# xor_lists(a, b) # [1, 3, 4, 6]
# 2) write a function named and_lists to combine two lists with items in both lists.
# example:
# a = [1, 2, 3]
# b = [2, 4, 6]
# and_lists(a, b) # [2]
# 3) write a function named left_lists to combine two lists with items from first list and not from second list
# example:
# a = [1, 2, 3]
# b = [2, 4, 6]
# left_lists(a, b) # [1, 3]


def xor_lists(a,b):
    result = z ^ y
    print(result)
    return result


def and_lists(a,b):
    result = z & y
    print(result)
    return result

def left_lists(a,b):
    result = z - y
    print(result)
    return result

if __name__ == "__main__":
    # a = [2,4,6,8]
    # b = [1,2,3,4,5,6,7,8]
    a = [1, 2, 3]
    b = [2, 4, 6]

    z = set(a)
    y = set(b)
    xor_lists(z,y)
    and_lists(z,y)
    left_lists(z,y)








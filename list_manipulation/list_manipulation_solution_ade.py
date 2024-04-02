from os import path, system
from sys import argv as argument

system('clear')


def xor_lists(a:list,b:list)->list:
    result = (set(a) | set(b)) - (set(a) & set(b))
    return list(result)


def and_lists(a:list,b:list)->list:
    return list(set(a) & set(b))


def left_lists(a:list,b:list)->list :
    return list(set(a) - set(b))


a = [1, 2, 3]
b = [2, 4, 6]

def main():
    print(xor_lists(a,b))
    print(and_lists(a,b))
    print(left_lists(a,b))

if __name__ == "__main__":
    main()
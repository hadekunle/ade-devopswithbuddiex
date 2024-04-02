def xor_lists(list1, list2):
    combined = []
    for value in list1:
        if value not in list2:
            combined.append(value)
    for value in list2:
        if value not in list1:
            combined.append(value)
    return combined

def and_lists(list1, list2):
    combined = []
    for value in list1:
        if value in list2:
            combined.append(value)
    return combined

def left_lists(list1, list2):
    combined = []
    for value in list1:
        if value not in list2:
            combined.append(value)
    return combined

def main():
    list1 = [1, 2, 3]
    list2 = [2, 4, 6]
    print("items in either list but not both:", xor_lists(list1, list2))
    print("items in both lists:", and_lists(list1, list2))
    print("items from first list and not from second list:", left_lists(list1, list2))

if __name__ == "__main__":
    main()
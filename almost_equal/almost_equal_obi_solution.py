
from pprint import pprint

def are_almost_equal(str1, str2):
    # Base case: 
    if str1 == str2:
        return False

    len1, len2 = len(str1), len(str2)

    # Case 1: Strings of equal length
    if len1 == len2:
        return sum(c1 != c2 for c1, c2 in zip(str1, str2)) == 1

    # Case 2: Length difference of 1, 
    if abs(len1 - len2) == 1:
        # Ensure str1 is the longer string
        if len1 < len2:
            str1, str2 = str2, str1

        for i in range(len(str1)):
            if str1[:i] + str1[i+1:] == str2:
                return True

    # If none of the above conditions are met, the strings are not almost equal
    return False


if __name__ == "__main__":
    a= "xyz"
    b="xyc"
    result = are_almost_equal(a,b)
    pprint(result)
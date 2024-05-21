from almost_equal_obi_solution import are_almost_equal
from pprint import pprint

test_cases = [
    ("xyz", "xyc", True),
    ("xyz", "xy", True),
    ("xyz", "xz", True),
    ("xyz", "yz", True),
    ("xyz", "xyzz", True),
    ("xyz", "xayz", True),
    ("x", "", True),
    ("xyz", "xyz", False),
    ("xyz", "xzy", False),
    ("xyz", "xk", False),
    ("xyz", "yzxt", False),
    # Additional test cases
    ("", "a", True),  # Test empty string and one char string
    ("abc", "abcde", False),  # Test strings with length difference more than 1
    ("abc", "abd", True),  # Test one char difference in the middle
    ("a", "b", True),  # Test single character difference
]

def run_test_cases(test_cases):
    results = []
    for str1, str2, expected in test_cases:
        result = are_almost_equal(str1, str2)
        results.append((str1, str2, result == expected, expected, result))
    return results


test_results = run_test_cases(test_cases)
pprint(test_results)
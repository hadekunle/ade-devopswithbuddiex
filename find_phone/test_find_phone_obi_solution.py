import pytest
from find_phone_Obi_solution import extract_valid_us_phone_numbers  

# Here's a modified function for direct input testing
def extract_from_string(input_string):
    # This is a stand-in for the original function that works with direct string input
    return extract_valid_us_phone_numbers(input_string)

@pytest.mark.parametrize("test_input,expected", [
    ("John Doe\t123-456-7890", ["123-456-7890"]),
    ("Jane Smith\t123.456.7891", ["123.456.7891"]),
    ("Sam Brown\t123 456 7892", ["123 456 7892"]),
    ("Alex Johnson\t(123) 456 7893", ["(123) 456 7893"]),
    ("Linda Harris\t(123)456-7894", ["(123)456-7894"]),
    ("Mike Wilson\t(123) 456.7898", ["(123) 456.7898"]),
    ("Rachel Adams\t123-456-789", []),  
    ("Brian Taylor\t123-456-ABCD", []),  
    ("Emily White\t456-7890", []),  
    ("David Brown\t  (123)  456 - 7899  ", ["(123)  456 - 7899"])  
])
def test_valid_us_phone_numbers(test_input, expected):
    # Simulate file reading by passing the string directly to the modified function
    assert extract_from_string(test_input) == expected

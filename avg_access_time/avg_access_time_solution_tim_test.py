import pytest
from avg_access_time_solution_tim import avg_access_time_calc

# Test case for file not found
def test_avg_access_time_calc_file_not_found(tmp_path):
    # Create a temporary file path that doesn't exist
    with pytest.raises(SystemExit) as excinfo:
        # Call the function with the non-existent file path
        avg_access_time_calc(tmp_path / "non_existent_file.txt")
    # Check if the system exits with code 1
    assert excinfo.value.code == 1

# Test case for incorrect format in the file
def test_avg_access_time_calc_incorrect_format(tmp_path):
    # Create a temporary file with incorrect format
    file_path = tmp_path / "incorrect_format.txt"
    with open(file_path, 'w') as f:
        f.write("invalid_format")
    # Call the function with the file containing incorrect format
    with pytest.raises(SystemExit) as excinfo:
        avg_access_time_calc(file_path)
    # Check if the system exits with code 1
    assert excinfo.value.code == 1

# Test case for correct processing of the file
def test_avg_access_time_calc_valid_input(tmp_path):
    # Create a temporary file with valid input
    file_path = tmp_path / "valid_input.txt"
    with open(file_path, 'w') as f:
        f.write("09:30:01 10-03-2020 98003 56dccecacba54a3 open\n")
        f.write("09:30:22 10-03-2020 98022 16dccecacba54a1 open\n")
        f.write("09:35:04 10-03-2020 98003 56dccecacba54a3 close\n")
        f.write("10:35:34 10-03-2020 98022 16dccecacba54a1 close\n")
        f.write("11:30:01 10-03-2020 98004 56dccecacba54a3 open\n")
        f.write("11:35:08 10-03-2020 98004 56dccecacba54a3 close\n")
    # Expected output after processing the file
    expected_output = '56dccecacba54a3 00:10:10\n16dccecacba54a1 01:05:12'

    # Call the function and check if the output matches the expected output
    assert avg_access_time_calc(file_path) == expected_output

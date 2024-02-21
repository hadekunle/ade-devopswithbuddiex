import pytest
import os
from datetime import datetime
import clear_things_up_solution_tim
from clear_things_up_solution_tim import time_tracker, time_calc

# Test case for correct processing of the input file
def test_time_tracker_valid_input():
    # Write data to the input file
    with open('valid_input.txt', 'w') as f:
        f.write('time date pid action\n')
        f.write('10:20:00 10/10/2020 1 start\n')
        f.write('10:22:40 10/12/2020 2 end\n')

    # Define the expected output
    expected_output = {'1': '2 days, 00:02:40'}

    # Call the time_tracker function with the input file
    valid_output = clear_things_up_solution_tim.time_tracker('valid_input.txt')

    # Check if the output matches the expected output
    assert valid_output == expected_output

    # Remove the temporary input file
    os.remove('valid_input.txt')

# Test case for file not found error
def test_time_tracker_file_not_found(tmp_path):
    with pytest.raises(SystemExit):
        clear_things_up_solution_tim.time_tracker(tmp_path / "non_existent_file.txt")

# Test case for incorrect date-time format
def test_time_calc_incorrect_format():
    with pytest.raises(ValueError):
        clear_things_up_solution_tim.time_calc("10/10/2020 8:00:00", "10/12/2020 10:22:40:21")

# Test case for correct calculation of time difference
def test_time_calc_valid_input():
    date_time1 = "10/10/2020 8:00:00"
    date_time2 = "10/12/2020 10:22:40"
    assert time_calc(date_time2, date_time1) == "2 days, 2:22:40"

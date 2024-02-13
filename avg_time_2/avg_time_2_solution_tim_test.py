import pytest
from datetime import timedelta
from avg_time_2_solution_tim import avg_time_calc, format_timedelta, average_timedelta

# Test cases for avg_time_calc function

# Test case for file not found
def test_avg_time_calc_file_not_found(tmp_path):
    with pytest.raises(SystemExit) as excinfo:
        avg_time_calc(tmp_path / "non_existent_file.txt")
    assert excinfo.value.code == 1

# Test case for incorrect format in the file
def test_avg_time_calc_incorrect_format(tmp_path):
    file_path = tmp_path / "incorrect_format.txt"
    with open(file_path, 'w') as f:
        f.write("invalid_format")
    with pytest.raises(SystemExit) as excinfo:
        avg_time_calc(file_path)
    assert excinfo.value.code == 1

# Test case for correct processing of the file
def test_avg_time_calc_valid_input(tmp_path):
    file_path = tmp_path / "valid_input.txt"
    with open(file_path, 'w') as f:
        f.write("interval 12:00:00 10/10/2020 - 13:00:00 10/10/2020\n")
        f.write("interval 08:00:00 10/10/2020 - 12:00:00 10/11/2020\n")

    # Modify the expected_timespan to match the returned format
    expected_timespan = (['01:00:00', '28:00:00'], '14:30:00')
    # Print for debugging purposes
    print("avg_time_calc:", avg_time_calc(file_path))
    print("expected_timespan:", expected_timespan)
    # Assertion
    assert avg_time_calc(file_path) == expected_timespan


# Test case for formatting timedelta with non-zero seconds
def test_format_timedelta():
    assert format_timedelta(timedelta(seconds=3661)) == "01:01:01"

# Test case for formatting timedelta with zero seconds
def test_format_timedelta_zero():
    assert format_timedelta(timedelta(seconds=0)) == "00:00:00"

# Test case for empty list of timedeltas
def test_average_timedelta_empty_list():
    assert average_timedelta([]) == timedelta(seconds=0)

# Test case for non-empty list of timedeltas
def test_average_timedelta_non_empty_list():
    timedeltas = [timedelta(seconds=3600), timedelta(seconds=7200)]
    assert average_timedelta(timedeltas) == timedelta(seconds=5400)

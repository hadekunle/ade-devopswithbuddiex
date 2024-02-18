from datetime import datetime, timedelta
import pytest
from clear_things_up_solution_ade import calculate_interval,time_fmt


def test_calculate_interval():
    start = end = str(datetime.now().strftime(time_fmt))
    print (type(calculate_interval(start,end)))
    # Test case for current time and itself
    assert str(calculate_interval(start,end)) == '0:00:00'
    # Test case for 1 hour, 1 min and 1 second diff
    assert str(calculate_interval('14:02:03 10/23/2020','15:03:04 10/23/2020')) == '1:01:01'
    # Test cases for different years
    assert str(calculate_interval('15:02:03 12/31/2023','14:02:03 1/1/2024')) == '23:00:00'
    # Test cases for midnight crossover
    assert str(calculate_interval('23:59:59 02/07/2024', '00:00:01 02/08/2024')) == '0:00:02'
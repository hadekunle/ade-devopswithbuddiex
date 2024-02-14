from datetime import datetime, timedelta

import pytest
from avg_time_2_solution_ade import calculate_interval,average_interval, time_fmt


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
    # Test case for 24 hours or more failed

def test_average_interval():
    # Test case for average of 0 and 2 hours
    test_1 = timedelta(hours=0, minutes=0, seconds=0)
    test_2 = timedelta(hours=2, minutes=0, seconds=0)
    assert average_interval([test_1,test_2]) == '1:00:00'
    # Test case for average of 15 and 60 minutes  
    test_3 = timedelta(hours=0, minutes=30, seconds=0)
    test_4 = timedelta(hours=0, minutes=60, seconds=0)
    assert average_interval([test_3,test_4]) == '0:45:00'
    # Test case for average of 10 and 20 seconds
    test_5 = timedelta(hours=0, minutes=0, seconds=10)
    test_6 = timedelta(hours=0, minutes=0, seconds=20)
    assert average_interval([test_5,test_6]) == '0:00:15'
    # Test case for two increment across the board
    test_7 = timedelta(hours=10, minutes=10, seconds=10)
    test_8 = timedelta(hours=12, minutes=12, seconds=12)
    assert average_interval([test_7,test_8]) == '11:11:11'
    # Test case for average of 0 and 1 increment
    test_9 = timedelta(hours=0, minutes=0, seconds=0)
    test_10 = timedelta(hours=1, minutes=1, seconds=1)
    assert average_interval([test_9,test_10]) == '0:30:30'
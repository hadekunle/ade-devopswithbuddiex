import pytest
from avg_time_2_Obi import avg_time  
from datetime import timedelta


def create_test_file(tmp_path, content):
    file_path = tmp_path / "test_intervals.txt"
    file_path.write_text(content)
    return str(file_path)


@pytest.mark.parametrize("content,expected", [
    ("Interval1 14:02:03 10/23/2020 - 14:05:03 10/23/2020", timedelta(minutes=3)),
    ("Interval1 14:02:03 10/23/2020 - 14:05:03 10/23/2020", timedelta(minutes=3)),
    ("Interval2 15:00:00 10/23/2020 - 15:03:00 10/23/2020", timedelta(minutes=3)),
    ("Interval1 14:02:03 10/23/2020 - 14:05:03 10/23/2020", timedelta(minutes=3))
])
def test_avg_time(tmp_path, content, expected):
    
    file_path = create_test_file(tmp_path, content)
    
    assert avg_time(file_path) == expected

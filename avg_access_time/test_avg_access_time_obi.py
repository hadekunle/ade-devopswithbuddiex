import pytest
from avg_access_time_Obi import average_time

def test_calculate_average_access_times(tmp_path):
    # Create a temporary log file
    log_file = tmp_path / "log_file.txt"
    log_file.write_text("""
09:30:01 10-03-2020 98003 56dccecacba54a3 open
09:35:04 10-03-2020 98003 56dccecacba54a3 close
09:30:22 10-03-2020 98022 16dccecacba54a1 open
10:35:34 10-03-2020 98022 16dccecacba54a1 close
""".strip())

   
    expected = [
        ("56dccecacba54a3", "00:05:03"),
        ("16dccecacba54a1", "01:05:12"),
          ]
    
    result = average_time(str(log_file))
    
    assert result == expected

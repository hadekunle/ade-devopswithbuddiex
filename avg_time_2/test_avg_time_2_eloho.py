import unittest
from unittest.mock import patch
from avg_time_2_eloho import avg_interval
import sys

class TestAvgAccessTime(unittest.TestCase):
    @patch('builtins.print')
    def test_avg_interval(self, mock_print):
        # Create a temporary log file for testing
        with open("temp_log.txt", "w") as file:
            file.write("Interval1 14:02:03 10/23/2020 - 14:05:03 10/23/2020\n")
            file.write("Interval2 14:10:00 10/23/2020 - 14:15:00 10/23/2020\n")

        # Test avg_interval with the temporary log file
        with patch.object(sys, 'argv', ['test_script.py', 'temp_log.txt']):
            avg_interval_result = avg_interval(sys.argv[1])

        # Clean up the temporary log file
        import os
        os.remove("temp_log.txt")

        # Check if the mocked print was called with the correct result
        mock_print.assert_called_with(type(avg_interval_result))

if __name__ == "__main__":
    unittest.main()

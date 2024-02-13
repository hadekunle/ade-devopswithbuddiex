import unittest
from unittest.mock import patch, mock_open
from avg_time_2_solution_ajibola import avg_time
from datetime import datetime, timedelta

class TestAvgtime(unittest.TestCase):
    @patch("builtins.open")
    def test_avg_time(self, mock_open):
        mock_open.return_value.__enter__.return_value = [
            "Interval1 14:02:03 10/23/2020 - 14:05:03 10/23/2020\n",
            "Interval2 19:07:33 10/24/2020 - 18:07:33 10/25/2020\n",
            "Interval3 04:23:11 10/25/2020 - 06:13:14 10/25/2020\n",
            "Interval4 12:01:55 10/26/2020 - 00:01:55 10/27/2020\n",
            "Interval5 08:00:45 10/27/2020 - 02:55:40 10/28/2020\n",
        ]
        
        # Call the avg_time function, because of patch decorator, this call will be intercepted with the test data above
        result = avg_time("fake/file/path")
        
        expected_average = timedelta(hours=11, minutes=9, seconds=35, microseconds=600000)
        self.assertEqual(result, expected_average, "The function didn't return the expected value")
        mock_open.assert_called_once_with("fake/file/path", "r")
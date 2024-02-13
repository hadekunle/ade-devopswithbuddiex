import unittest
from unittest.mock import patch, mock_open
from avg_access_time_solution_ajibola import avg_time
from datetime import datetime, timedelta

class TestAvgaccess(unittest.TestCase):
    @patch("builtins.open")
    def test_avg_time(self, mock_open):
        mock_open.return_value.__enter__.return_value = [
            "09:30:01 10-03-2020 98003 56dccecacba54a3 open\n",
            "09:30:22 10-03-2020 98022 16dccecacba54a1 open\n",
            "09:35:04 10-03-2020 98003 56dccecacba54a3 close\n",
            "10:35:34 10-03-2020 98022 16dccecacba54a1 close\n",
            "11:30:01 10-03-2020 98004 56dccecacba54a3 open\n",
            "11:35:08 10-03-2020 98004 56dccecacba54a3 close\n"
        ]

        # Call the avg_time function, because of patch decorator, this call will be intercepted with the test data above
        result = avg_time("fake/file/path")
        
        expected_average = {'56dccecacba54a3': [timedelta(seconds=610), 2], '16dccecacba54a1': [timedelta(seconds=3912), 1]}
        self.assertEqual(result, expected_average, "The function didn't return the expected value")
        mock_open.assert_called_once_with("fake/file/path", "r")
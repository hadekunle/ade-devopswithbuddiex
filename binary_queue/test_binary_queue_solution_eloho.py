import unittest
import binary_queue_solution_eloho as bq
import os
from unittest.mock import patch, call, mock_open
from collections import defaultdict
import datetime
from io import StringIO

class TestBinaryQueue(unittest.TestCase):

    
    def setUp(self):
        self.tempfile = "test_file"
        self.tempfile_output = "test_output"


    def tearDown(self):
        if os.path.exists(self.tempfile):
            os.remove(self.tempfile)

        if os.path.exists(self.tempfile_output):
            os.remove(self.tempfile_output)


    @patch("sys.argv", ["binary_queue_solution_eloho.py", "test_file"])
    def test_process_file(self):
        with open(self.tempfile, "w") as f:
            f.write("binary created_at status\n")
            f.write("b1 10:00:00 01/01/2021 running\n")
            f.write("b2 10:00:00 01/01/2021 queued\n")
            f.write("b3 10:00:00 01/01/2021 stopped\n")
        expected = {'b1': [(datetime.datetime(2021, 1, 1, 10, 0), 'running')], 'b2': [(datetime.datetime(2021, 1, 1, 10, 0), 'queued')], 'b3': [(datetime.datetime(2021, 1, 1, 10, 0), 'stopped')]}


        result = bq.process_file(self.tempfile)
        self.assertEqual(result, expected)

    def test_check_status(self):
        data = {'b1': [(datetime.datetime(2021, 1, 1, 10, 0), 'running')], 'b2': [(datetime.datetime(2021, 1, 1, 10, 0), 'queued')], 'b3': [(datetime.datetime(2021, 1, 1, 10, 0), 'stopped')]}
        expected = {'b1': [(datetime.datetime(2021, 1, 1, 10, 0), 'running')], 'b2': [(datetime.datetime(2021, 1, 1, 10, 0), 'queued')]}

        self.assertEqual(bq.check_status(data), expected)


    def test_custom_sort(self):
        item = (datetime.datetime(2021, 1, 1, 10, 0), 'running')
        result = bq.custom_sort(item)
        expected = ('running', datetime.datetime(2021, 1, 1, 10, 0))
        self.assertEqual(result, expected)
  
        
if __name__ == "__main__":
    unittest.main()
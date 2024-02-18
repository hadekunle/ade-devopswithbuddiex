import clear_things_up_solution_eloho
import unittest
import datetime
import io
import os
from unittest.mock import patch

class TestClearThingsUpSolutionEloho(unittest.TestCase):

    @patch('sys.argv', ['clear_things_up_solution_eloho.py', 'test_file.txt'])
    def test_process_file(self):

        with open('test_file.txt', 'w') as f:
            f.write('time date pid action\n')
            f.write('10:00:00 01/01/2021 1 start\n')
            f.write('10:01:00 01/01/2021 1 end\n')
            f.write('10:00:00 01/01/2021 2 start\n')
            f.write('10:02:00 01/01/2021 2 end\n')
            f.write('10:00:00 01/01/2021 3 start\n')
            f.write('10:03:00 01/01/2021 3 end\n')
        
        result = clear_things_up_solution_eloho.process_file('test_file.txt')
        expected = { '1': [datetime.datetime(2021, 1, 1, 10, 0), {'time_spent': datetime.timedelta(seconds=60)}],
                     '2': [datetime.datetime(2021, 1, 1, 10, 0), {'time_spent': datetime.timedelta(seconds=120)}],
                     '3': [datetime.datetime(2021, 1, 1, 10, 0), {'time_spent': datetime.timedelta(seconds=180)}]
                   }
        
        self.assertEqual(result, expected)
        os.remove('test_file.txt')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_result(self, mock_stdout):
        data = { '1': [datetime.datetime(2021, 1, 1, 10, 0), {'time_spent': datetime.timedelta(seconds=60)}],
                 '2': [datetime.datetime(2021, 1, 1, 10, 0), {'time_spent': datetime.timedelta(seconds=120)}],
                 '3': [datetime.datetime(2021, 1, 1, 10, 0), {'time_spent': datetime.timedelta(seconds=180)}]
               }
        
        expected = '1 0:01:00\n2 0:02:00\n3 0:03:00\n'
        clear_things_up_solution_eloho.output_result(data)
        self.assertEqual(mock_stdout.getvalue(), expected)
    

    



if __name__ == "__main__":
    unittest.main()
    os.remove('test_file.txt')

            
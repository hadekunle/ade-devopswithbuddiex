import unittest
import os
from clear_mess_solution_eloho import clear_mess

class TestClearMess(unittest.TestCase):

    def setUp(self):
        # Create a temporary file with messy data for testing
        self.temp_file = "temp_test_file.txt"
        with open(self.temp_file, "w") as f:
            f.write("a123-456-789012/34/5678\n")
            f.write("b456-789-012301/23/4567\n")
            f.write("c789-012-345678/90/1234\n")

    def tearDown(self):
        # Remove the temporary file after the test
        os.remove(self.temp_file)

    def test_clear_mess(self):
        expected_result = {'a': {'phone_number': '123-456-7890', 'start_date': '12/34/5678'},
                           'b': {'phone_number': '456-789-0123', 'start_date': '01/23/4567'},
                           'c': {'phone_number': '789-012-3456', 'start_date': '78/90/1234'}}

        result = clear_mess(self.temp_file)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

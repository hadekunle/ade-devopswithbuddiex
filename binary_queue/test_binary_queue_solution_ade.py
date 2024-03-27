from datetime import datetime, timedelta
import pytest
from binary_queue_solution_ade import parser
import os

def test_parser():
    test_check_file = 'test_check_file.txt'
    check_file_content = 'Test binary created_at status\nb7 11:05:40 10/15/2022 queued\nb7 11:05:40 10/15/2020 queued'
    
    test_report_file = 'test_report_file.txt'
    
    expected=['b7 11:05:40 10/15/2020 queued\n', 'b7 11:05:40 10/15/2022 queued\n']
    expected=[each.strip() for each in expected]
    
    with open (test_check_file,'w') as file:
        file.write(check_file_content)
    
    result = parser(test_check_file,test_report_file)
            
    os.remove(test_check_file)
    os.remove(test_report_file)

    assert result == expected
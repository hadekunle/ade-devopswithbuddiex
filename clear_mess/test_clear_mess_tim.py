import pytest
import os
from tempfile import TemporaryDirectory
from clear_mess_tim import read_messed_up_file, messed_up_file_split, create_file_with_format

@pytest.fixture
def test_data():
    """Fixture to create a temporary file with test data."""
    data = [
        "Alice415-123-456710/09/2019",
        "415-908-9999Bob10/10/2019",
        "10/10/2019Charlie549-000-1234",
        "10/12/2019Dave312-999-1234",
        "Eve415-123-456910/31/2019",
        "415-908-1002Frank10/25/2019",
        "10/29/2019Grace549-000-1231"
    ]
    with TemporaryDirectory() as tmp_dir:
        tmp_file = os.path.join(tmp_dir, "test_data.txt")
        with open(tmp_file, "w") as f:
            f.write("\n".join(data))
        yield tmp_file

def test_read_messed_up_file(test_data):
    """Test read_messed_up_file function."""
    lines = read_messed_up_file(test_data)
    assert lines == [
        "Alice415-123-456710/09/2019",
        "415-908-9999Bob10/10/2019",
        "10/10/2019Charlie549-000-1234",
        "10/12/2019Dave312-999-1234",
        "Eve415-123-456910/31/2019",
        "415-908-1002Frank10/25/2019",
        "10/29/2019Grace549-000-1231"
    ]

def test_messed_up_file_split(test_data):
    """Test messed_up_file_split function."""
    lines = read_messed_up_file(test_data)
    results = messed_up_file_split(lines)
    assert results == [
        {'Username': 'Alice', 'Phone_num': '415-123-4567', 'Start_date': '10/09/2019'},
        {'Phone_num': '415-908-9999', 'Username': 'Bob', 'Start_date': '10/10/2019'},
        {'Start_date': '10/10/2019', 'Username': 'Charlie', 'Phone_num': '549-000-1234'},
        {'Start_date': '10/12/2019', 'Username': 'Dave', 'Phone_num': '312-999-1234'},
        {'Username': 'Eve', 'Phone_num': '415-123-4569', 'Start_date': '10/31/2019'},
        {'Phone_num': '415-908-1002', 'Username': 'Frank', 'Start_date': '10/25/2019'},
        {'Start_date': '10/29/2019', 'Username': 'Grace', 'Phone_num': '549-000-1231'}
    ]

def test_create_file_with_format(test_data):
    """Test create_file_with_format function."""
    create_file_with_format(test_data)
    with open('result_file', 'r') as file:
        content = file.read()
    assert content == (
        "Username Phone_num Start_date\n"
        "Alice 415-123-4567 10/09/2019\n"
        "Bob 415-908-9999 10/10/2019\n"
        "Charlie 549-000-1234 10/10/2019\n"
        "Dave 312-999-1234 10/12/2019\n"
        "Eve 415-123-4569 10/31/2019\n"
        "Frank 415-908-1002 10/25/2019\n"
        "Grace 549-000-1231 10/29/2019\n"
    )

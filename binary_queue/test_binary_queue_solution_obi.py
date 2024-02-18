import pytest
import tempfile
import os
from binary_queue_solution_obi import process_binaries  

# Helper function to create a temporary file with initial content and return its path
def create_temp_file(content):
    temp = tempfile.NamedTemporaryFile(delete=False)
    with open(temp.name, 'w') as f:
        f.write(content)
    return temp.name

# Helper function to read content from a file
def read_file_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()

@pytest.mark.parametrize("initial_content,expected_result", [
    # Test Case 1: Empty File
    ("binary created_at date status\n", "binary created_at date status\n"),
    # Test Case 2: All Binaries Completed
    ("binary created_at date status\nb1 10:05:04 10/15/2020 succeeded\nb2 11:05:06 10/15/2020 failed\n", "binary created_at date status\n"),
    # Test Case 3: All Binaries Queued
    ("binary created_at date status\nb1 14:05:06 10/15/2020 queued\nb2 12:04:04 10/15/2020 queued\n", "binary created_at date status\nb2 12:04:04 10/15/2020 queued\nb1 14:05:06 10/15/2020 queued\n"),
    # Test Case 4: Mixed Statuses Without Reordering
    ("binary created_at date status\nb1 10:05:04 10/15/2020 running\nb2 11:05:40 10/15/2020 queued\nb3 12:05:00 10/15/2020 queued\n", "binary created_at date status\nb2 11:05:40 10/15/2020 queued\nb3 12:05:00 10/15/2020 queued\nb1 10:05:04 10/15/2020 running\n"),
    # Test Case 5: Complex Mix Requiring Sorting and Removal
    ("binary created_at date status\nb1 10:05:04 10/15/2020 running\nb2 13:05:06 10/15/2020 queued\nb3 11:07:24 10/15/2020 succeeded\nb4 12:04:04 10/15/2020 queued\nb5 13:05:00 10/15/2020 failed\n", "binary created_at date status\nb4 12:04:04 10/15/2020 queued\nb2 13:05:06 10/15/2020 queued\nb1 10:05:04 10/15/2020 running\n"),
])
def test_process_binaries(initial_content, expected_result):
    # Create a temporary file with the initial content
    file_path = create_temp_file(initial_content)
    
    # Process the binaries
    process_binaries(file_path)
    
    # Verify the file content against the expected result
    assert read_file_content(file_path) == expected_result
    
    # Clean up
    os.remove(file_path)

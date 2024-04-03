import os
import pytest
from binary_queue_solution_tim import read_file, update_file

# Test cases for read_file function
def test_read_file_file_not_found(tmp_path):
    with pytest.raises(SystemExit) as excinfo:
        read_file(tmp_path / "non_existent_file.txt")
    assert excinfo.value.code == 1

def test_read_file_valid_input(tmp_path):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, 'w') as f:
        f.write("binary1 12:00:00 running\n")
        f.write("binary2 13:00:00 queued\n")
    lines = read_file(file_path)
    assert len(lines) == 2

# Test cases for update_file function
def test_update_file_valid_input(tmp_path):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, 'w') as f:
        f.write("binary1 12:00:00 running\n")
        f.write("binary2 13:00:00 queued\n")
    lines = read_file(file_path)
    update_file(lines, file_path)
    with open(file_path, 'r') as f:
        updated_lines = f.readlines()
    assert len(updated_lines) == 2
    assert updated_lines[0].strip() == "binary2 13:00:00 queued"
    assert updated_lines[1].strip() == "binary1 12:00:00 running"

def test_update_file_invalid_time_format(tmp_path):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, 'w') as f:
        f.write("binary1 12:00:00 running\n")
        f.write("binary2 invalid_time queued\n")
    lines = read_file(file_path)
    with pytest.raises(SystemExit) as excinfo:
        update_file(lines, file_path)
    assert excinfo.value.code == 1

def test_update_file_unable_to_write(tmp_path):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, 'w') as f:
        f.write("binary1 12:00:00 running\n")
        f.write("binary2 13:00:00 queued\n")
    os.chmod(file_path, 0o400)  # Change permissions to make the file read-only
    lines = read_file(file_path)
    with pytest.raises(SystemExit) as excinfo:
        update_file(lines, file_path)
    assert excinfo.value.code == 1

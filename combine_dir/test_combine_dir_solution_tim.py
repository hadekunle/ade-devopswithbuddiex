import os

import pytest
from combine_dir_solution_tim import combine_directories, copy_file

# Define test functions
def test_copy_file(tmpdir):
    # Create temporary source and destination files
    src_file = os.path.join(tmpdir, 'src_file.txt')
    dest_file = os.path.join(tmpdir, 'dest_file.txt')
    # Write content to source file
    with open(src_file, 'wb') as f:
        f.write(b'This is a test file content')
    # Call the function to test
    copy_file(src_file, dest_file)
    # Check if destination file exists and has the same content as source file
    assert os.path.exists(dest_file)
    with open(dest_file, 'rb') as f:
        assert f.read() == b'This is a test file content'


def test_combine_directories(tmpdir):
    # Create temporary directories for testing
    dir1_backup = os.path.join(tmpdir, 'dir1_backup')
    os.makedirs(os.path.join(dir1_backup, 'sub_dir1'))  # Create subdirectory 'sub_dir1'
    dir2_backup = os.path.join(tmpdir, 'dir2_backup')
    os.makedirs(os.path.join(dir2_backup, 'sub_dir2'))  # Create subdirectory 'sub_dir2'
    new_dir_tim = os.path.join(tmpdir, 'new_dir_tim')
    # Create some files in the directories
    with open(os.path.join(dir1_backup, 'file1.txt'), 'w') as f:
        f.write('This is file1 from dir1_backup')
    with open(os.path.join(dir1_backup, 'sub_dir1', 'file2.txt'), 'w') as f:
        f.write('This is file2 from dir1_backup')
    with open(os.path.join(dir2_backup, 'file3.txt'), 'w') as f:
        f.write('This is file3 from dir2_backup')
    with open(os.path.join(dir2_backup, 'sub_dir2', 'file4.txt'), 'w') as f:
        f.write('This is file4 from dir2_backup')
    # Call the function to test
    combine_directories(dir1_backup, dir2_backup, new_dir_tim)
    # Check if files are correctly copied to new_dir_tim
    assert os.path.exists(os.path.join(new_dir_tim, 'file1.txt'))
    assert os.path.exists(os.path.join(new_dir_tim, 'sub_dir1', 'file2.txt'))
    assert os.path.exists(os.path.join(new_dir_tim, 'file3.txt'))
    assert os.path.exists(os.path.join(new_dir_tim, 'sub_dir2', 'file4.txt'))


if __name__ == '__main__':
    pytest.main([__file__])


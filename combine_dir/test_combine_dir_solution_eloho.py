import unittest
import os
import tempfile
import shutil
from combine_dir_solution_eloho import combine_dir

class TestCombineDir(unittest.TestCase):

    def setUp(self):
        self.test_dir1 = tempfile.mkdtemp()
        self.test_dir2 = tempfile.mkdtemp()
        self.test_new_dir = tempfile.mkdtemp()

        # Create some test files and directories in test_dir1 and test_dir2
        test_file1 = os.path.join(self.test_dir1, "file1.txt")
        test_file2 = os.path.join(self.test_dir2, "file2.txt")
        test_dir1_subdir = os.path.join(self.test_dir1, "subdir1")
        test_dir2_subdir = os.path.join(self.test_dir2, "subdir2")

        os.mkdir(test_dir1_subdir)
        os.mkdir(test_dir2_subdir)

        with open(test_file1, 'w') as f:
            f.write("Content from file1")

        with open(test_file2, 'w') as f:
            f.write("Content from file2")

    def test_combine_dir(self):
        combine_dir(self.test_dir1, self.test_dir2, self.test_new_dir)

        # Check if files from dir1 are in new_dir
        self.assertTrue(os.path.exists(os.path.join(self.test_new_dir, "file1.txt")))

        # Check if files from dir2 are in new_dir
        self.assertTrue(os.path.exists(os.path.join(self.test_new_dir, "file2.txt")))

        # Check if subdirectories are created
        self.assertTrue(os.path.exists(os.path.join(self.test_new_dir, "subdir1")))
        self.assertTrue(os.path.exists(os.path.join(self.test_new_dir, "subdir2")))

    def tearDown(self):
        # Clean up temporary directories
        shutil.rmtree(self.test_dir1)
        shutil.rmtree(self.test_dir2)
        shutil.rmtree(self.test_new_dir)

if __name__ == '__main__':
    unittest.main()
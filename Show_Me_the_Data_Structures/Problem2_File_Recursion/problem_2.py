import os
import unittest
import time


def recursive_traversal(suffix, path, selected_files):

    for i in os.listdir(path):
        sub_path = os.path.join(path, i)

        if os.path.isfile(sub_path):

            if sub_path.endswith(suffix):
                selected_files.append(sub_path)
        else:
            recursive_traversal(suffix, sub_path, selected_files)


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if len(path.strip()) ==0:
        return "Path is empty."

    if not os.path.exists(path.strip()):
        return "No such path found."

    path = os.path.normpath(path)

    if len(suffix.strip()) < 2 or suffix.strip()[0] != '.':
        return "Suffix is not valid."

    selected_files = []

    recursive_traversal(suffix.strip(), path.strip(), selected_files)

    if len(selected_files) == 0:
        return "No such suffix found."

    return selected_files


found = find_files(".c", ".")
print(found if isinstance(found, (str,)) else '\n'.join('{}'.format(k) for k in found))

# My unit tests

# For a clear display
print('\n\n\n\n\n')
time.sleep(0.1)


class FindFilesTest(unittest.TestCase):

    def test_empty_path(self):
        found = find_files(".c", "   ")
        self.assertEqual(found, "Path is empty.")

    def test_no_found_path(self):
        found = find_files(".c", "./python")
        self.assertEqual(found, "No such path found.")

    def test_no_valid_suffix(self):
        found = find_files("c", ".")
        self.assertEqual(found, "Suffix is not valid.")

    def test_find_files(self):
        found = find_files(".c", ".")
        self.assertEqual(set(found), {'./t.c',
                                 './testdir/subdir3/subsubdir1/b.c',
                                 './testdir/t1.c',
                                 './testdir/subdir1/a.c',
                                 './testdir/subdir5/a.c'})

    def test_find_files_sub_dir(self):

        found = find_files(".c", "./testdir/subdir1/")
        self.assertEqual(found, ['testdir/subdir1/a.c'])

    def test_no_found(self):
        found = find_files(".java", ".")
        self.assertEqual(found, "No such suffix found.")


suite_loader = unittest.TestLoader()
suite = suite_loader.loadTestsFromTestCase(FindFilesTest)
unittest.TextTestRunner(verbosity=2).run(suite)








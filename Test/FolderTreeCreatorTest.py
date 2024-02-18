import unittest
from Test import FolderCreator
from Controler import FolderTreeCreator


class FolderTreeCreatorTest(unittest.TestCase):
    def test_folder_tree_creator_low(self):
        nest_level = 1
        folder_creator_low = FolderCreator("D:\\", root_folder_name="TestsLow", nest_level=nest_level, folders_number=5, files_number=5)
        folder_tree_creator_low = FolderTreeCreator(folder_creator_low.root_folder, nest_level=nest_level)

        try:
            self.assertEqual(sorted(folder_tree_creator_low.folder_list), sorted(folder_creator_low.folders_list))
            print("Low Test Passed")
        finally:
            folder_creator_low.clean_up()

    def test_folder_tree_creator_mid(self):
        nest_level = 2
        folder_creator_mid = FolderCreator("D:\\", root_folder_name="TestsMid", nest_level=nest_level, folders_number=4, files_number=4)
        folder_tree_creator_mid = FolderTreeCreator(folder_creator_mid.root_folder, nest_level=nest_level)

        try:
            self.assertEqual(sorted(folder_tree_creator_mid.folder_list), sorted(folder_creator_mid.folders_list))
            print("Mid Test Passed")
        finally:
            folder_creator_mid.clean_up()

    def test_folder_tree_creator_heavy(self):
        nest_level = 3
        folder_creator_heavy = FolderCreator("D:\\", root_folder_name="TestsHigh", nest_level=nest_level, folders_number=2, files_number=2)
        folder_tree_creator_heavy = FolderTreeCreator(folder_creator_heavy.root_folder, nest_level=nest_level)

        try:
            self.assertEqual(sorted(folder_tree_creator_heavy.folder_list), sorted(folder_creator_heavy.folders_list))
            print("Heavy Test Passed")
        finally:
            folder_creator_heavy.clean_up()


if __name__ == '__main__':
    unittest.main()

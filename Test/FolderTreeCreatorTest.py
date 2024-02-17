import unittest
from Test import FolderCreator
from Controler import FolderTreeCreator


class FolderTreeCreatorTest(unittest.TestCase):
    def test_folder_tree_creator_low(self):
        nest_level = 1
        folder_creator = FolderCreator("D:\\", nest_level=nest_level, folders_number=5, files_number=5)
        folder_tree_creator = FolderTreeCreator(folder_creator.root_folder, nest_level=nest_level)

        try:
            self.assertEqual(folder_tree_creator.folder_list, folder_creator.folders_list)
        finally:
            folder_creator.clean_up()

    def test_folder_tree_creator_mid(self):
        nest_level = 2
        folder_creator = FolderCreator("D:\\", nest_level=nest_level, folders_number=5, files_number=10)
        folder_tree_creator = FolderTreeCreator(folder_creator.root_folder, nest_level=nest_level)

        try:
            self.assertEqual(folder_tree_creator.folder_list, folder_creator.folders_list)
        finally:
            folder_creator.clean_up()

    def test_folder_tree_creator_heavy(self):
        nest_level = 3
        folder_creator = FolderCreator("D:\\", nest_level=nest_level, folders_number=10, files_number=10)
        folder_tree_creator = FolderTreeCreator(folder_creator.root_folder, nest_level=nest_level)

        try:
            self.assertEqual(folder_tree_creator.folder_list, folder_creator.folders_list)
        finally:
            folder_creator.clean_up()


if __name__ == '__main__':
    unittest.main()

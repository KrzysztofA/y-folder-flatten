import os
import unittest
from TestUtils import FolderCreator, FileListCreator
from Controler import FolderTreeCreator, Unpacker


class UnpackerTest(unittest.TestCase):
    def test_unpacker_low(self):
        nest_level = 1
        files_number = 3
        folders_number = 3
        creator = FolderCreator(root_folder="D:\\", root_folder_name="LowTest", nest_level=nest_level, files_number=files_number, folders_number=folders_number)
        tree_creator = FolderTreeCreator(nest_level=nest_level, root_folder=creator.root_folder)
        unpacker = Unpacker(root_folder=creator.root_folder, delete_empty_after_moving=True, rename_on_failed=True)
        for i in reversed(tree_creator.get()):
            unpacker.folder_flatten(i)
        list_creator = FileListCreator(root_folder=creator.root_folder, nest_level=nest_level, files_number=files_number, folders_number=folders_number)
        file_list = [os.path.join(creator.root_folder, i) for i in os.listdir(creator.root_folder)]
        try:
            self.assertEqual(sorted(file_list), sorted(list_creator.file_list))
        finally:
            for i in reversed(file_list):
                os.remove(i)
            creator.clean_up()

    def test_unpacker_mid(self):
        nest_level = 2
        files_number = 4
        folders_number = 4
        creator = FolderCreator(root_folder="D:\\", root_folder_name="MidTest", nest_level=nest_level, files_number=files_number, folders_number=folders_number)
        tree_creator = FolderTreeCreator(nest_level=nest_level, root_folder=creator.root_folder)
        unpacker = Unpacker(root_folder=creator.root_folder, delete_empty_after_moving=True, rename_on_failed=True)
        for i in reversed(tree_creator.get()):
            unpacker.folder_flatten(i)
        list_creator = FileListCreator(root_folder=creator.root_folder, nest_level=nest_level, files_number=files_number, folders_number=folders_number)
        file_list = [os.path.join(creator.root_folder, i) for i in os.listdir(creator.root_folder)]
        try:
            self.assertEqual(sorted(file_list), sorted(list_creator.file_list))
        finally:
            for i in reversed(file_list):
                os.remove(i)
            creator.clean_up()

    def test_unpacker_high(self):
        nest_level = 3
        files_number = 3
        folders_number = 5
        creator = FolderCreator(root_folder="D:\\", root_folder_name="HighTest", nest_level=nest_level, files_number=files_number, folders_number=folders_number)
        tree_creator = FolderTreeCreator(nest_level=nest_level, root_folder=creator.root_folder)
        unpacker = Unpacker(root_folder=creator.root_folder, delete_empty_after_moving=True, rename_on_failed=True)
        for i in reversed(tree_creator.get()):
            unpacker.folder_flatten(i)
        list_creator = FileListCreator(root_folder=creator.root_folder, nest_level=nest_level, files_number=files_number, folders_number=folders_number)
        file_list = [os.path.join(creator.root_folder, i) for i in os.listdir(creator.root_folder)]
        try:
            self.assertEqual(sorted(file_list), sorted(list_creator.file_list))
        finally:
            for i in reversed(file_list):
                os.remove(i)
            creator.clean_up()


if __name__ == '__main__':
    unittest.main()

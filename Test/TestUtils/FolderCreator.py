import os
from typing import List


class FolderCreator:
    root_folder: str
    items_list: List[str] = []
    folders_list: List[str] = []

    def __init__(self, root_folder: str = "./", folder_name: str = "test", nest_level: int = 1, folders_number: int = 1, file_name: str = "test", files_number: int = 1):
        self.root_folder = root_folder

    def change_root_folder(self, root_folder: str):
        self.root_folder = root_folder

    def create_nested_folders_with_files_at_root(self, nest_level: int, folder_name: str, folders_number: int, file_name: str, files_number: int):
        def create_dir(folder_path):
            os.mkdir(folder_path)
            self.folders_list.append(folder_path)

        if nest_level >= 1:
            last_folder = 0
            for i in range(0, nest_level):
                if i == 0:
                    for j in range(0, folders_number):
                        full_path = os.path.join(self.root_folder, folder_name + f"_{j}")
                        create_dir(full_path)
                        self.create_files_in_folder(full_path, file_name, files_number)
                else:
                    temp_last_folder = len(self.folders_list)
                    for k in range(last_folder, len(self.folders_list)):
                        for j in range(0, folders_number):
                            full_path = os.path.join(self.folders_list[k], folder_name + f"_{j}")
                            create_dir(full_path)
                            self.create_files_in_folder(full_path, file_name, files_number)
                    last_folder = temp_last_folder

    def create_files_in_folder(self, folder_path: str, file_name: str, files_number: int):
        for i in range(0, files_number):
            file_path = os.path.join(folder_path, file_name) + f"_{i}.txt"
            with open(file_path, 'w') as new_file:
                pass
            self.items_list.append(file_path)

    def clean_up(self):
        for i in range(len(self.items_list), 0, -1):
            os.remove(self.items_list[i])
        for i in range(len(self.folders_list), 0, -1):
            os.removedirs(self.folders_list[i])

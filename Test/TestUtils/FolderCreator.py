import os
from typing import List
from pathlib import PurePath


class FolderCreator:
    def __init__(self, root_folder: str = "./", root_folder_name: str = "Tests", folder_name: str = "test", nest_level: int = 1, folders_number: int = 1, file_name: str = "test", files_number: int = 1):
        self.root_folder = os.path.join(root_folder, root_folder_name)
        self.items_list: List[str] = []
        self.folders_list: List[PurePath] = []
        try:
            os.mkdir(self.root_folder)
        except FileExistsError:
            print(f"{self.root_folder} already exists!")
        self.create_nested_folders_with_files_at_root(nest_level=nest_level, folder_name=folder_name, files_number=files_number, folders_number=folders_number, file_name=file_name)

    def change_root_folder(self, root_folder: str):
        self.root_folder = root_folder

    def create_nested_folders_with_files_at_root(self, nest_level: int, folder_name: str, folders_number: int, file_name: str, files_number: int):
        def create_dir(folder_path):
            try:
                os.mkdir(folder_path)
                self.folders_list.append(PurePath(folder_path))
            except FileExistsError:
                print(f"{folder_path} already exists!")

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
        try:
            for i in reversed(self.items_list):
                os.remove(i)
        except FileNotFoundError:
            pass
        try:
            for i in reversed(self.folders_list):
                os.removedirs(i)
        except FileNotFoundError:
            pass
        try:
            os.removedirs(self.root_folder)
        except FileNotFoundError:
            pass

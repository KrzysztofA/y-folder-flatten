import os
from typing import List
from pathlib import PurePath


class FolderTreeCreator:
    def __init__(self, root_folder: str, nest_level: int = 1):
        self.root_folder = root_folder
        self.nest_level = nest_level
        self.folder_list: List[PurePath] = []
        self.update_list()

    def change_root(self, root_folder: PurePath | str):
        self.root_folder = root_folder
        self.update_list()

    def change_nest_level(self, new_nest_level: int):
        self.nest_level = new_nest_level
        self.update_list()

    def update_list(self):
        self.folder_list = self.__create_nest_dir_list(self.root_folder)
        level_indexes = [0, len(self.folder_list)]
        for i in range(1, self.nest_level):
            for j in range(level_indexes[i - 1], level_indexes[i]):
                temp_dirs = self.__create_nest_dir_list(self.folder_list[j])
                for k in temp_dirs:
                    self.folder_list.append(k)
            level_indexes.append(len(self.folder_list))

    def get_root(self) -> str | PurePath:
        return self.root_folder

    def get_nest_level(self) -> int:
        return self.nest_level

    def get(self) -> List[PurePath]:
        return self.folder_list

    @staticmethod
    def __create_nest_dir_list(dst_path):
        return [PurePath(dst_path, j) for j in os.listdir(dst_path) if os.path.isdir(PurePath(dst_path, j))]

import math
from typing import List
import os


class FileListCreator:
    def __init__(self, root_folder: str = "./Tests", nest_level: int = 1, folders_number: int = 1, file_name: str = "test", files_number: int = 1):
        self.file_list: List[str] = []
        num: int = int((1-math.pow(folders_number, nest_level + 1))/(1-folders_number)) - 1

        for i in range(0, num):
            for j in range(0, files_number):
                if i == 0:
                    self.file_list.append(os.path.join(root_folder, f"{file_name}_{j}.txt"))
                else:
                    self.file_list.append(os.path.join(root_folder, f"{file_name}_{j}_{i}.txt"))

from dataclasses import dataclass
import os
import os.path
from pathlib import PurePath, Path
import shutil


@dataclass
class Unpacker:
    root_folder: str | PurePath
    delete_empty_after_moving: bool = True
    rename_on_failed: bool = True
    multi_name_suffix: str = "_<n>"

    def name_builder(self, filename: str | PurePath | Path, number: int) -> PurePath:
        path_no_ext, ext = os.path.splitext(filename)
        if number == 0:
            return PurePath(filename)
        if not str.__contains__(self.multi_name_suffix, "<n>"):
            return PurePath(path_no_ext + self.multi_name_suffix + str(number) + ext)
        return PurePath(path_no_ext + str.replace(self.multi_name_suffix, "<n>", str(number)) + ext)

    def name_renamer(self, filename: str | PurePath, number: int) -> PurePath:
        if number == 0:
            return PurePath(filename)
        else:
            old_path = Path(self.name_builder(filename, number - 1))
            new_path = self.name_builder(filename, number)
            return old_path.rename(new_path)

    def folder_flatten(self, dst_path):
        dir_list = os.listdir(dst_path)
        for name in dir_list:
            file_name = os.path.join(dst_path, name)
            current_try = 0
            success = False
            while not success:
                src = self.name_renamer(file_name, current_try)
                try:
                    shutil.move(src, self.root_folder)
                    success = True
                    if self.delete_empty_after_moving and dst_path is not self.root_folder and not len(os.listdir(dst_path)) > 0:
                        os.removedirs(dst_path)
                except shutil.Error:
                    if self.rename_on_failed:
                        current_try += 1
                    else:
                        pass

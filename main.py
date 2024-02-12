import os
import os.path
import shutil

root_folder: str = ""
nest_level: int = 0

while not os.path.isdir(root_folder):
    root_folder = input("Enter the root folder path: ")

while not isinstance(nest_level, int) or nest_level < 1:
    try:
        nest_level = int(input("Enter how many levels of nest you want to flatten: "))
    except:
        nest_level = 0


def folder_flatten(dst_path):
    dir_list = os.listdir(dst_path)
    for name in dir_list:
        src = os.path.join(dst_path, name)
        try:
            shutil.move(src, root_folder)
            if dst_path is not root_folder:
                os.removedirs(dst_path)
        except:
            print("Invalid Operation, continuing")


def move_nest_level(dst_path):
    dir_list = os.listdir(dst_path)
    dir_dir_list = []
    for name in dir_list:
        src = os.path.join(dst_path, name)
        if os.path.isdir(src):
            dir_dir_list.append(src)
    return dir_dir_list


all_dirs = [root_folder]
level_indexes = [0]
for i in range(1, nest_level):
    for j in range (level_indexes[i - 1], len(all_dirs)):
        temp_dirs = move_nest_level(all_dirs[j])
        for k in temp_dirs:
            all_dirs.append(k)
    level_indexes.append(len(all_dirs))

for i in reversed(all_dirs):
    folder_flatten(i)

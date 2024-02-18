import os.path
from Controler import FolderTreeCreator, Unpacker


class CommandLineApplication:
    def __init__(self):

        root_folder: str = ""
        nest_level: int = 0

        while not os.path.isdir(root_folder):
            root_folder = input("Enter the root folder path: ")
            if os.path.isdir(f"./{root_folder}"):
                print("Relative Path provided, restart if not intended")
                root_folder = f"./{root_folder}"
                break

        while not isinstance(nest_level, int) or nest_level < 1:
            try:
                nest_level = int(input("Enter how many levels of nest you want to flatten: "))
            except ValueError:
                nest_level = 0

        valid_input = ['y', 'n']
        bool_input = ''

        while not valid_input.__contains__(bool_input):
            bool_input = input("Rename file on failed move? y/n")

        rename_on_failed = bool_input == "y"

        while not valid_input.__contains__(bool_input):
            bool_input = input("Delete empty folders after moving? y/n")

        delete_empty_folders = bool_input == "y"

        while not valid_input.__contains__(bool_input):
            bool_input = input("By continuing you agree that the owner is not responsible on your files and system integrity. You acknowledge "
                               "that the application wasn't tested on thoroughly and on all systems. y/n")

        if bool_input == "y":
            tree_creator = FolderTreeCreator(root_folder, nest_level)
            unpacker = Unpacker(root_folder=root_folder, rename_on_failed=rename_on_failed,
                                delete_empty_after_moving=delete_empty_folders)
            for i in reversed(tree_creator.get()):
                unpacker.folder_flatten(i)


if __name__ == "__main__":
    app = CommandLineApplication()

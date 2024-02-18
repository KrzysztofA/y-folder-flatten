import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from Controler import FolderTreeCreator, Unpacker
from View import DirectoryFrame
import os


class TKInterApplication:
    root_folder: str = ""
    auto_rename_duplicates: bool = False
    auto_delete_empty_folder: bool = False
    nest_level: int = 1

    def __init__(self):
        window = Tk()
        window.resizable(False, False)
        auto_rename_duplicates_input = BooleanVar()

        def rename_dups_callback(var, index, mode):
            self.set_auto_rename_duplicates(auto_rename_duplicates_input.get())

        auto_rename_duplicates_input.trace_add(mode="write", callback=rename_dups_callback)
        auto_delete_empty_folder_input = BooleanVar()

        def auto_delete_callback(var, index, mode):
            self.set_auto_delete_empty_folder(auto_delete_empty_folder_input.get())

        auto_delete_empty_folder_input.trace_add(mode="write", callback=auto_delete_callback)
        nest_level_input = StringVar(value="1")

        def nest_level_callback(var, index, mode):
            self.set_nest_level_from_string(nest_level_input.get())

        nest_level_input.trace_add(mode="write", callback=nest_level_callback)

        window.title("y-folder-flatten")
        mainframe = ttk.Frame(window, padding="5 5 5 5", width=300, height=100)
        mainframe.grid_columnconfigure(0, weight=1, uniform="foo")
        mainframe.grid_columnconfigure(1, weight=1, uniform="foo")
        mainframe.grid_columnconfigure(2, weight=1, uniform="foo")
        mainframe.grid_rowconfigure(0, weight=1, uniform="foo")
        mainframe.grid_rowconfigure(1, weight=1, uniform="foo")
        mainframe.grid_rowconfigure(2, weight=1, uniform="foo")
        mainframe.grid_rowconfigure(3, weight=1, uniform="foo")
        mainframe.grid_rowconfigure(4, weight=1, uniform="foo")
        mainframe.grid_rowconfigure(5, weight=1, uniform="foo")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root_folder_entry_label = ttk.Label(mainframe, text="Root Folder")
        root_folder_entry_frame = DirectoryFrame(mainframe, self.set_root_folder)

        nest_level_spinbox_label = ttk.Label(mainframe, text="Nest Level")
        nest_level_spinbox = ttk.Spinbox(mainframe, from_=1.0, to=100.0, textvariable=nest_level_input, width=5)
        rename_dups_check_label = ttk.Label(mainframe, text="Auto-Rename Duplicates")
        rename_dups_check = ttk.Checkbutton(mainframe, variable=auto_rename_duplicates_input, onvalue=True)
        auto_delete_check_label = ttk.Label(mainframe, text="Auto-Delete Empty Folder")
        auto_delete_check = ttk.Checkbutton(mainframe, variable=auto_delete_empty_folder_input, onvalue=True)
        execute_button = ttk.Button(mainframe, text="Execute", command=self.execute_app)
        self.error_label = ttk.Label(mainframe, text="", foreground="red")

        root_folder_entry_label.grid(column=0, row=0)
        root_folder_entry_frame.grid(column=0, row=1, columnspan=2)

        nest_level_spinbox_label.grid(column=2, row=0)
        nest_level_spinbox.grid(column=2, row=1, columnspan=1)
        rename_dups_check_label.grid(column=0, row=2)
        rename_dups_check.grid(column=2, row=2, columnspan=1)
        auto_delete_check_label.grid(column=0, row=3)
        auto_delete_check.grid(column=2, row=3, columnspan=1)
        execute_button.grid(row=4)
        self.error_label.grid(row=5, column=0, columnspan=3)

        window.mainloop()

    def execute_app(self):
        if not os.path.isdir(self.root_folder):
            if os.path.isdir(f"./{self.root_folder}"):
                self.root_folder = "./" + self.root_folder
            else:
                self.error_label.config(text="Invalid directory, not matching both relative and global paths")

        if tkinter.messagebox.askokcancel("y-folder-flatten",
                                          "By continuing you agree that the owner is not responsible on your files and system integrity. You acknowledge "
                                          "that the application wasn't tested on thoroughly and on all systems."):

            tree_creator = FolderTreeCreator(self.root_folder, self.nest_level)
            unpacker = Unpacker(root_folder=self.root_folder, rename_on_failed=self.auto_rename_duplicates,
                                delete_empty_after_moving=self.auto_delete_empty_folder)
            for i in reversed(tree_creator.get()):
                unpacker.folder_flatten(i)

    def set_auto_rename_duplicates(self, auto_rename_duplicates: bool):
        self.auto_rename_duplicates = auto_rename_duplicates

    def set_auto_delete_empty_folder(self, auto_delete_empty_folder: bool):
        self.auto_delete_empty_folder = auto_delete_empty_folder

    def set_root_folder(self, root_folder: str):
        self.root_folder = root_folder

    def set_nest_level_from_string(self, new_nest_level: str):
        try:
            self.nest_level = int(new_nest_level)
        except ValueError:
            # Set error label to error
            self.error_label.config(text="Nest Level has value error")


if __name__ == "__main__":
    app = TKInterApplication()

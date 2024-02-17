from tkinter import *
from tkinter import ttk, filedialog
from typing import Callable


class DirectoryFrame(ttk.Frame):
    held_string: str = ""

    def __init__(self, master: Misc | None, callback: Callable[[str], object]):
        super().__init__(master)
        popup = Menu(self, tearoff=0)

        self.entry_input = StringVar()

        def input_call(var, index, mode):
            self.held_string = self.entry_input.get()
            callback(self.entry_input.get())

        self.entry_input.trace_add(mode="write", callback=input_call)

        main_entry = ttk.Entry(self, textvariable=self.entry_input, width=50)

        def delete_command():
            temp = self.clipboard_get()
            main_entry.event_generate("<<Cut>>")
            self.clipboard_clear()
            self.clipboard_append(temp)

        popup.add_command(label="Copy", command=lambda: main_entry.event_generate("<<Copy>>"))
        popup.add_command(label="Paste", command=lambda: main_entry.event_generate("<<Paste>>"))
        popup.add_command(label="Cut", command=lambda: main_entry.event_generate("<<Cut>>"))
        popup.add_command(label="Delete", command=delete_command)

        def menu_popup(event):
            try:
                popup.tk_popup(event.x_root, event.y_root, 0)
            finally:
                # Release the grab
                popup.grab_release()

        main_entry.bind("<Button-3>", menu_popup)


        def open_directory():
            directory = filedialog.askdirectory()
            self.entry_input.set(directory)

        open_root_folder_button = ttk.Button(self, text="Open", command=open_directory)
        main_entry.grid(column=0, row=0, columnspan=2)
        open_root_folder_button.grid(column=2, row=0)

    def get(self) -> str:
        return self.held_string

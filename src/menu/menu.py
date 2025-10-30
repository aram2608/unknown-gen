import tkinter as tk
from tkinter import messagebox

class GramMenu(tk.Menu):
    def __init__(self, master: tk.Tk, exit: function):
        """
        Custom Menu class for our application

        Args:
            master is the root of the main Tkinter application
            exit is an exit command we pass in from the root
        """
        super().__init__(
            master=master,
        )
        self._create_menu(exit)

    def _create_menu(self, exit: function):
        self.file_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Info", menu=self.file_menu)
        # We only have an about command for now since that is all that is needed
        self.file_menu.add_command(
            label="About",
            command=lambda: messagebox.showinfo(
                "About unknown-gen",
                "unknown-gen v1.0\n\n"
                "Developed by: Javier Arambula Rascon\n"
                "© 2025 All Rights Reserved.",
            ),
        )
        # We add a small separator to make it look nicer
        self.file_menu.add_separator()
        # We contsruct the exit option using the exit command we pass in at init
        # TODO: Find a better solution since this is fragile
        self.file_menu.add_command(label="Exit", command=exit)

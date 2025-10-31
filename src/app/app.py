import tkinter as tk
from ..ui.frame.frame import GramFrame, ControlFrame
from ..controller.controller import Controller
from ..ui.menu.menu import GramMenu

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller: Controller = Controller()
        self.title("Unknown Bacteria Generator")
        self.geometry("600x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self._make_frames()
        self.menubar: tk.Menu = GramMenu(self, self.quit)
        self.config(menu=self.menubar)

    def _make_frames(self):
        # We populate each frame
        # We first create the gram positive frame and place it in the first row
        self.gram_pos_frame = GramFrame(
            self, "Gram Positive", "Example: S. aureus", self.controller
        )
        self.gram_pos_frame.grid(row=0, column=0, sticky="NSEW")

        # We can now create the gram negative frame and move it down one row
        self.gram_neg_fram = GramFrame(
            self, "Gram Negative", "Example: E. coli", self.controller
        )
        self.gram_neg_fram.grid(row=1, column=0, sticky="NSEW")

        # Finally we create the control frame, this frame contains the main
        # logic for generating files
        self.control_frame = ControlFrame(self, self.controller)
        self.control_frame.grid(row=2, column=0, sticky="NSEW")

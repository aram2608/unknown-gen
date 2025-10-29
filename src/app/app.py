import tkinter as tk
from ..frame.frame import Frame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "Unknown Bacteria Generator"
        self.geometry("600x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)
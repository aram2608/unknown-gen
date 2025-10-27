import tkinter as tk
from tkinter import ttk

class GUIWrapper:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Unknown Bacteria Generator")
        self.root.geometry("800x800")

    def run_gui(self):
        self.root.mainloop()
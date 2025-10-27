import tkinter as tk
from tkinter import ttk


class GUIWrapper:
    def __init__(self):
        # Root frame
        self.construct_root()

        # Frame 1 for gram positive bacteria
        self.construct_gram_pos()

        # Frame 2 for gram negative bacteria
        self.construct_gram_neg()

        # Frame 3 for showing the added bacteria
        self.construct_list_p()
        self.construct_list_n()

        # We initialize some empty lists to store our random bacteria
        self.gram_pos_list = []
        self.gram_neg_list = []

    def construct_root(self):
        """Small helper to construct the root frame."""
        self.root = tk.Tk()
        self.root.title("Unknown Bacteria Generator")
        self.root.geometry("800x800")

    def construct_gram_pos(self):
        """Small helper to construct the gram positive frame."""
        self.gram_pos = tk.Frame(self.root)
        self.gram_pos.grid(row=0, column=0)

        self.gram_p_lbl = tk.Label(self.gram_pos, text="Add Gram-Positive Bacteria")
        self.gram_p_lbl.grid(row=0, column=0)
        self.add_gp = tk.Button(
            self.gram_pos, text="Add New", command=self.add_gram_pos
        )
        self.add_gp.grid(row=0, column=1)
        self.gram_p_entry = tk.Entry(self.gram_pos)
        self.gram_p_entry.grid(row=0, column=3)

    def construct_gram_neg(self):
        """Small helper to construct the gram negative frame."""
        self.gram_neg = tk.Frame(self.root)
        self.gram_neg.grid(row=1, column=0)

        self.gram_n_lbl = tk.Label(self.gram_neg, text="Add Gram-Positive Bacteria")
        self.gram_n_lbl.grid(row=0, column=0)
        self.add_gn = tk.Button(
            self.gram_neg, text="Add New", command=self.add_gram_neg
        )
        self.add_gn.grid(row=0, column=1)
        self.gram_n_entry = tk.Entry(self.gram_neg)
        self.gram_n_entry.grid(row=0, column=3)

    def construct_list_p(self):
        self.pos_list_frame = tk.Frame(self.root)
        self.pos_list_frame.grid(row=2, column=0)
        self.list_p_txt = tk.Label(
            self.pos_list_frame, text="No bacteria added"
        )
        self.list_p_txt.grid(row=0, column=0)

    def construct_list_n(self):
        self.neg_list_frame = tk.Frame(self.root)
        self.neg_list_frame.grid(row=3, column=0)
        self.list_n_txt = tk.Label(
            self.neg_list_frame, text="No bacteria added"
        )
        self.list_n_txt.grid(row=0, column=0)

    def run_gui(self):
        self.root.mainloop()

    def add_gram_pos(self):
        current_text = self.gram_p_entry.get()
        if current_text != "":
            self.gram_p_entry.delete(0, tk.END)
            if current_text not in self.gram_pos_list:
                self.gram_pos_list.append(current_text)
                list_text = ", ".join(self.gram_pos_list)
                self.list_p_txt.config(text=list_text)

    def add_gram_neg(self):
        current_text = self.gram_n_entry.get()
        if current_text != "":
            self.gram_n_entry.delete(0, tk.END)
            if current_text not in self.gram_neg_list:
                self.gram_neg_list.append(current_text)
                list_text = ", ".join(self.gram_neg_list)
                self.list_n_txt.config(text=list_text)
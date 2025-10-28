import tkinter as tk
from tkinter import messagebox
from enum import Enum, auto

from .generator import generate_excel


class Palette(Enum):
    DARK = auto()
    LIGHT = auto()


class GUIWrapper:
    def __init__(self):
        # Load in our color palette
        self.lood_dark_palette()
        self.palette = Palette.DARK
        # Root frame
        self.construct_root()

        # Frame 1 for gram positive bacteria
        self.construct_gram_pos()

        # Frame 2 for gram negative bacteria
        self.construct_gram_neg()

        # Frame 3 for generation buttons
        self.construct_generate()

        # We initialize some empty lists to store our random bacteria
        self.gram_pos_list = []
        self.gram_neg_list = []

        self.sections = None
        self.student_count = None
        self.file_name = None

    def run_gui(self):
        """Main method to run the tkinter loop."""
        self.root.mainloop()

    def lood_dark_palette(self):
        """Helper to load in dark palette."""
        self.FRAME_BG = "#333A40"
        self.HIGHLIGHT = "#00BFA5"
        self.TEXT_FG = "#EAEAEA"
        self.BUTTON_BG = "#4C545C"
        self.BUTTON_FG = "#181616"
        self.ENTRY_BG = "#2C3136"
        self.ENTRY_FG = self.TEXT_FG

    def construct_root(self):
        """Small helper to construct the root frame."""
        self.root = tk.Tk()
        self.root.title("Unknown Bacteria Generator")
        self.root.geometry("600x600")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(3, weight=1)

    def construct_gram_pos(self):
        """Small helper to construct the gram positive frame."""

        # We need to create a base frame and position it in the root frame
        # This is the very first frame inside of the root
        self.gram_pos_frame = tk.Frame(
            self.root,
            highlightbackground=self.HIGHLIGHT,
            highlightthickness=2,
            bg=self.FRAME_BG,
        )
        self.gram_pos_frame.grid(row=0, column=0, sticky="NSEW")

        self.gram_pos_frame.columnconfigure(1, weight=1)

        # We now need to create input frames and widgets for adding gram positive
        # bacteria
        self.gram_p_lbl = tk.Label(
            self.gram_pos_frame,
            text="Gram-Positive Bacteria",
            bg=self.FRAME_BG,
            fg=self.TEXT_FG,
            font=("Arial", 14, "bold"),
        )
        self.gram_p_lbl.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        # We add a button that can call our add gram positive function
        self.add_gp = tk.Button(
            self.gram_pos_frame,
            text="Add New Bacteria",
            command=self.add_gram_pos,
            bg=self.BUTTON_BG,
            fg=self.BUTTON_FG,
            activebackground=self.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=5,
        )
        self.add_gp.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="W")

        # We can now add an entry box for adding in the bacteria
        self.gram_p_entry = tk.Entry(
            self.gram_pos_frame, bg=self.ENTRY_BG, fg=self.ENTRY_FG, relief="flat"
        )
        self.gram_p_entry.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="W")

        # We make an example label to help out users, that updates to show
        # which bacteria have been entered
        self.list_p_txt = tk.Label(
            self.gram_pos_frame,
            text="Example: S. aureus",
            wraplength=200,
            justify=tk.LEFT,
            bg=self.FRAME_BG,
            fg=self.TEXT_FG,
            font=("Arial", 10, "italic"),
        )
        self.list_p_txt.grid(row=2, column=1, padx=(5, 10), pady=(0, 10), sticky="W")

    def construct_gram_neg(self):
        """Small helper to construct the gram negative frame."""
        # We need to create a base frame and position it in the root frame
        # The gram negative frame is a row under the gram positive frame
        self.gram_neg_frame = tk.Frame(
            self.root,
            highlightbackground=self.HIGHLIGHT,
            highlightthickness=2,
            bg=self.FRAME_BG,
        )
        self.gram_neg_frame.grid(row=1, column=0, sticky="NSEW")
        self.gram_neg_frame.columnconfigure(1, weight=1)

        # We now need to create input frame and widgets for adding gram negative
        # bacteria
        self.gram_n_lbl = tk.Label(
            self.gram_neg_frame,
            text="Gram-Negative Bacteria",
            bg=self.FRAME_BG,
            fg=self.TEXT_FG,
            font=("Arial", 14, "bold"),
        )
        self.gram_n_lbl.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        # We need to add a button that can call our add gram neg function
        self.add_gn = tk.Button(
            self.gram_neg_frame,
            text="Add New Bacteria",
            command=self.add_gram_neg,
            bg=self.BUTTON_BG,
            fg=self.BUTTON_FG,
            activebackground=self.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=5,
        )
        self.add_gn.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="W")

        # We can now enter an entry box for our bacteria
        self.gram_n_entry = tk.Entry(
            self.gram_neg_frame, bg=self.ENTRY_BG, fg=self.ENTRY_FG, relief="flat"
        )
        self.gram_n_entry.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="W")

        self.list_n_txt = tk.Label(
            self.gram_neg_frame,
            text="Example: E. coli",
            wraplength=200,
            justify=tk.LEFT,
            bg=self.FRAME_BG,
            fg=self.TEXT_FG,
            font=("Arial", 10, "italic"),
        )
        self.list_n_txt.grid(row=2, column=1, padx=(5, 10), pady=(0, 10), sticky="W")

    def construct_generate(self):
        """Small helper to create the generate bacteria widget"""
        self.generate_frame = tk.Frame(
            self.root,
            highlightbackground=self.HIGHLIGHT,
            highlightthickness=2,
            bg=self.FRAME_BG,
        )
        self.generate_frame.grid(row=2, column=0, sticky="NSEW")
        self.generate_frame.columnconfigure(1, weight=1)

        # We need to create an input field and labels for the number of sections
        self.show_sections_lbl = tk.Label(
            self.generate_frame,
            text="Please provide the number of sections",
            bg=self.FRAME_BG,
            fg=self.TEXT_FG,
            font=("Arial", 11, "bold"),
        )
        self.show_sections_lbl.grid(
            row=0, column=1, pady=(10, 2), padx=(0, 10), sticky="W"
        )

        self.add_section_btn = tk.Button(
            self.generate_frame,
            text="Add number of sections",
            command=self.add_section_number,
            bg=self.BUTTON_BG,
            fg=self.BUTTON_FG,
            activebackground=self.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=5,
        )
        self.add_section_btn.grid(row=1, column=0, padx=(10, 5), pady=2, sticky="W")

        self.add_section_entry = tk.Entry(
            self.generate_frame, bg=self.ENTRY_BG, fg=self.ENTRY_FG, relief="flat"
        )
        self.add_section_entry.grid(row=1, column=1, padx=(0, 10), pady=2, sticky="EW")

        # We need to do the same for the number of students per class
        self.student_count_label = tk.Label(
            self.generate_frame,
            text="Please provide number of students per class",
            bg=self.FRAME_BG,
            fg=self.TEXT_FG,
            font=("Arial", 11, "bold"),
        )
        self.student_count_label.grid(
            row=2, column=1, pady=(10, 2), padx=(0, 10), sticky="W"
        )

        self.student_count_btn = tk.Button(
            self.generate_frame,
            text="Add students per class",
            command=self.add_student_number,
            bg=self.BUTTON_BG,
            fg=self.BUTTON_FG,
            activebackground=self.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=5,
        )
        self.student_count_btn.grid(row=3, column=0, padx=(10, 5), pady=2, sticky="W")

        self.student_count_entry = tk.Entry(
            self.generate_frame, bg=self.ENTRY_BG, fg=self.ENTRY_FG, relief="flat"
        )
        self.student_count_entry.grid(
            row=3, column=1, padx=(0, 10), pady=2, sticky="EW"
        )

        # We need to create an input field for the file name to be written
        self.file_name_lbl = tk.Label(
            self.generate_frame,
            text="Please provide the file name",
            bg=self.FRAME_BG,
            fg=self.TEXT_FG,
            font=("Arial", 11, "bold"),
        )
        self.file_name_lbl.grid(row=4, column=1, pady=(10, 2), padx=(0, 10), sticky="W")

        self.file_name_btn = tk.Button(
            self.generate_frame,
            text="Add the file name",
            command=self.add_file_name,
            bg=self.BUTTON_BG,
            fg=self.BUTTON_FG,
            activebackground=self.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=5,
        )
        self.file_name_btn.grid(row=5, column=0, padx=(10, 5), pady=2, sticky="W")

        self.file_name_entry = tk.Entry(
            self.generate_frame, bg=self.ENTRY_BG, fg=self.ENTRY_FG, relief="flat"
        )
        self.file_name_entry.grid(row=5, column=1, padx=(0, 10), pady=2, sticky="EW")

        # The final field we need to make is the generate random bacteria button
        self.generate_btn = tk.Button(
            self.generate_frame,
            text="Generate Random Bacteria",
            command=self.generate_random,
            bg=self.HIGHLIGHT,
            fg=self.BUTTON_FG,
            activebackground=self.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=6,
        )
        self.generate_btn.grid(row=6, column=0, padx=(10, 5), pady=15, sticky="W")

        self.status = tk.Label(
            self.generate_frame,
            text="Not generated",
            bg=self.FRAME_BG,
            fg=self.TEXT_FG,
            font=("Arial", 12, "bold"),
        )
        self.status.grid(row=6, column=1, sticky="W", padx=10, pady=15)

        # We can now add a little about button to show the application info
        self.about = tk.Button(
            self.generate_frame,
            text="About",
            command=lambda: messagebox.showinfo(
                "About unknown-gen",
                "unknown-gen v1.0\n\n"
                "Developed by: Javier Arambula Rascon\n"
                "© 2025 All Rights Reserved.",
            ),
            bg=self.BUTTON_BG,
            fg=self.BUTTON_FG,
            activebackground=self.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=5,
        )
        self.about.grid(row=7, column=1, padx=10, pady=(5, 10), sticky="E")

    def add_gram_pos(self):
        """Small helper to store a new gram positive bacteria."""
        # We retrieve the underlying data from the entry
        current_text = self.gram_p_entry.get()
        # We need to make sure its not empty before storing
        if current_text != "":
            self.gram_p_entry.delete(0, tk.END)
            # We do a test to make sure there are not duplicates
            if current_text not in self.gram_pos_list:
                self.gram_pos_list.append(current_text)
                list_text = ", ".join(self.gram_pos_list)
                self.list_p_txt.config(text=list_text)

    def add_gram_neg(self):
        """Small helper to store a new gram negative bacteria."""
        # We retrieve the underlying data from the entry
        current_text = self.gram_n_entry.get()
        # We need to make sure its not empty before storing
        if current_text != "":
            self.gram_n_entry.delete(0, tk.END)
            #  We do a test to make sure there are not duplicates
            if current_text not in self.gram_neg_list:
                self.gram_neg_list.append(current_text)
                list_text = ", ".join(self.gram_neg_list)
                self.list_n_txt.config(text=list_text)

    def add_section_number(self):
        """Small helper to add the number of class sections."""
        # We first retrieve the underlying data from the entry field
        current_num = self.add_section_entry.get()
        # We try and cast the number so we can store it properly
        try:
            current_num = int(current_num)
        # If it fails we assume a bad input
        except Exception as e:
            self.show_sections_lbl.config(text="Invalid input for number of sections")
        # Otherwise we go ahead and try to store the number
        else:
            # We need to check that the number is greater than 0 and not empty
            if current_num > 0 and current_num != "":
                self.add_section_entry.delete(0, tk.END)
                self.sections = current_num
                self.show_sections_lbl.config(text=f"{self.sections} total sections")
            else:
                self.add_section_entry.delete(0, tk.END)
                self.show_sections_lbl.config(
                    text="Please provide a number greater than 0"
                )

    def add_student_number(self):
        """Small helper to retrieve the number of students per class."""
        # We retrive the underlying data from the entry field
        current_num = self.student_count_entry.get()
        # We now try to cast it as an integer so we can store it properly
        try:
            current_num = int(current_num)
        # If it fails we assume their was a ba input
        except Exception as e:
            self.student_count_label.config(text="Invalid input for number of students")
        # If the cast was a success we can try and store the number
        else:
            # We first need to check that the number is greater than 0
            if current_num > 0 and current_num != "":
                self.student_count_entry.delete(0, tk.END)
                self.student_count = current_num
                self.student_count_label.config(
                    text=f"{self.student_count} total students"
                )
            else:
                self.student_count_label.config(
                    text="Please provide a number greater than 0"
                )

    def add_file_name(self):
        """Small helper to retrive file name from the field."""
        # We first retrive the underlying data from the entry
        current_file_name = self.file_name_entry.get()
        # We can now ensure it is not empty
        if current_file_name != "":
            self.file_name_entry.delete(0, tk.END)
            self.file_name = current_file_name
            self.file_name_lbl.config(text=f"Provided file name: {self.file_name}.xlsx")
        else:
            self.file_name_lbl.config(text="Please provide a valid name")

    def generate_random(self):
        """Function providing the main logic for creating the generated file."""
        # We first need to ensure that all of the default values have been provided
        if (
            self.file_name is not None
            and self.student_count is not None
            and self.sections is not None
        ):
            # We then need to test that at least one of each bacteria has been
            # provided
            if len(self.gram_pos_list) > 0 and len(self.gram_neg_list) > 0:
                # We then try and generate the file and store the returned bool
                result = generate_excel(
                    gramp_list=self.gram_pos_list,
                    gramn_list=self.gram_neg_list,
                    sections=self.sections,
                    range_size=self.student_count,
                    file_name=self.file_name,
                )
                # We can now inform the user about the success of the run
                if result:
                    self.status.config(text="Succesfully generated file")
                else:
                    self.status.config(text="Failed to generate file")

import tkinter as tk
from .generator import generate_excel

class Controller:
    def __init__(self):
        self.gram_postive = []
        self.gram_negative = []
        self.file_name = None
        self.student_count = None
        self.sections = None

    def add_bacteria(self, name, entry, text_label):
        """Small helper to store a new gram positive bacteria."""
        # We retrieve the underlying data from the entry
        text = entry.get()
        # We need to make sure its not empty before storing
        if text != "":
            entry.delete(0, tk.END)
            # We do a test to make sure there are no duplicates
            # We also need to test the name and make sure it matches the proper
            # bacteria type
            if name == "Gram Positive" and text not in self.gram_postive:
                self.gram_postive.append(text)
                list_text = ", ".join(self.gram_postive)
                text_label.config(text=list_text)
            elif name == "Gram Negative" and text not in self.gram_negative:
                self.gram_negative.append(text)
                list_text = ", ".join(self.gram_negative)
                text_label.config(text=list_text)

    def add_section_number(self, entry, label):
        """Small helper to add the number of class sections."""
        # We first retrieve the underlying data from the entry field
        current_num = entry.get()
        # We try and cast the number so we can store it properly
        try:
            current_num = int(current_num)
        # If it fails we assume a bad input
        except Exception as e:
            label.config(text="Invalid input for number of sections")
        # Otherwise we go ahead and try to store the number
        else:
            # We need to check that the number is greater than 0 and not empty
            if current_num > 0 and current_num != "":
                entry.delete(0, tk.END)
                self.sections = current_num
                label.config(text=f"{self.sections} total sections")
            else:
                entry.delete(0, tk.END)
                label.config(text="Please provide a number greater than 0")

    def add_student_number(self, entry, label):
        """Small helper to retrieve the number of students per class."""
        # We retrive the underlying data from the entry field
        current_num = entry.get()
        # We now try to cast it as an integer so we can store it properly
        try:
            current_num = int(current_num)
        # If it fails we assume their was a ba input
        except Exception as e:
            label.config(text="Invalid input for number of students")
        # If the cast was a success we can try and store the number
        else:
            # We first need to check that the number is greater than 0
            if current_num > 0 and current_num != "":
                entry.delete(0, tk.END)
                self.student_count = current_num
                label.config(text=f"{self.student_count} total students")
            else:
                label.config(text="Please provide a number greater than 0")

    def add_file_name(self, entry, label):
        """Small helper to retrive file name from the field."""
        # We first retrive the underlying data from the entry
        current_file_name = entry.get()
        # We can now ensure it is not empty
        if current_file_name != "":
            entry.delete(0, tk.END)
            self.file_name = current_file_name
            label.config(text=f"Provided file name: {self.file_name}.xlsx")
        else:
            label.config(text="Please provide a valid name")

    def generate_random(self, status):
        """Function providing the main logic for creating the generated file."""
        # We first need to ensure that all of the default values have been provided
        if (
            self.file_name is not None
            and self.student_count is not None
            and self.sections is not None
        ):
            # We then need to test that at least one of each bacteria has been
            # provided
            if len(self.gram_postive) > 0 and len(self.gram_negative) > 0:
                # We then try and generate the file and store the returned bool
                result = generate_excel(
                    gramp_list=self.gram_postive,
                    gramn_list=self.gram_negative,
                    sections=self.sections,
                    range_size=self.student_count,
                    file_name=self.file_name,
                )
                # We can now inform the user about the success of the run
                if result:
                    status.config(text="Succesfully generated file")
                else:
                    status.config(text="Failed to generate file")

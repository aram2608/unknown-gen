# def add_gram_pos(self):
#         """Small helper to store a new gram positive bacteria."""
#         # We retrieve the underlying data from the entry
#         current_text = self.gram_p_entry.get()
#         # We need to make sure its not empty before storing
#         if current_text != "":
#             self.gram_p_entry.delete(0, tk.END)
#             # We do a test to make sure there are not duplicates
#             if current_text not in self.gram_pos_list:
#                 self.gram_pos_list.append(current_text)
#                 list_text = ", ".join(self.gram_pos_list)
#                 self.list_p_txt.config(text=list_text)

#     def add_gram_neg(self):
#         """Small helper to store a new gram negative bacteria."""
#         # We retrieve the underlying data from the entry
#         current_text = self.gram_n_entry.get()
#         # We need to make sure its not empty before storing
#         if current_text != "":
#             self.gram_n_entry.delete(0, tk.END)
#             #  We do a test to make sure there are not duplicates
#             if current_text not in self.gram_neg_list:
#                 self.gram_neg_list.append(current_text)
#                 list_text = ", ".join(self.gram_neg_list)
#                 self.list_n_txt.config(text=list_text)

#     def add_section_number(self):
#         """Small helper to add the number of class sections."""
#         # We first retrieve the underlying data from the entry field
#         current_num = self.add_section_entry.get()
#         # We try and cast the number so we can store it properly
#         try:
#             current_num = int(current_num)
#         # If it fails we assume a bad input
#         except Exception as e:
#             self.show_sections_lbl.config(text="Invalid input for number of sections")
#         # Otherwise we go ahead and try to store the number
#         else:
#             # We need to check that the number is greater than 0 and not empty
#             if current_num > 0 and current_num != "":
#                 self.add_section_entry.delete(0, tk.END)
#                 self.sections = current_num
#                 self.show_sections_lbl.config(text=f"{self.sections} total sections")
#             else:
#                 self.add_section_entry.delete(0, tk.END)
#                 self.show_sections_lbl.config(
#                     text="Please provide a number greater than 0"
#                 )

#     def add_student_number(self):
#         """Small helper to retrieve the number of students per class."""
#         # We retrive the underlying data from the entry field
#         current_num = self.student_count_entry.get()
#         # We now try to cast it as an integer so we can store it properly
#         try:
#             current_num = int(current_num)
#         # If it fails we assume their was a ba input
#         except Exception as e:
#             self.student_count_label.config(text="Invalid input for number of students")
#         # If the cast was a success we can try and store the number
#         else:
#             # We first need to check that the number is greater than 0
#             if current_num > 0 and current_num != "":
#                 self.student_count_entry.delete(0, tk.END)
#                 self.student_count = current_num
#                 self.student_count_label.config(
#                     text=f"{self.student_count} total students"
#                 )
#             else:
#                 self.student_count_label.config(
#                     text="Please provide a number greater than 0"
#                 )

#     def add_file_name(self):
#         """Small helper to retrive file name from the field."""
#         # We first retrive the underlying data from the entry
#         current_file_name = self.file_name_entry.get()
#         # We can now ensure it is not empty
#         if current_file_name != "":
#             self.file_name_entry.delete(0, tk.END)
#             self.file_name = current_file_name
#             self.file_name_lbl.config(text=f"Provided file name: {self.file_name}.xlsx")
#         else:
#             self.file_name_lbl.config(text="Please provide a valid name")

#     def generate_random(self):
#         """Function providing the main logic for creating the generated file."""
#         # We first need to ensure that all of the default values have been provided
#         if (
#             self.file_name is not None
#             and self.student_count is not None
#             and self.sections is not None
#         ):
#             # We then need to test that at least one of each bacteria has been
#             # provided
#             if len(self.gram_pos_list) > 0 and len(self.gram_neg_list) > 0:
#                 # We then try and generate the file and store the returned bool
#                 result = generate_excel(
#                     gramp_list=self.gram_pos_list,
#                     gramn_list=self.gram_neg_list,
#                     sections=self.sections,
#                     range_size=self.student_count,
#                     file_name=self.file_name,
#                 )
#                 # We can now inform the user about the success of the run
#                 if result:
#                     self.status.config(text="Succesfully generated file")
#                 else:
#                     self.status.config(text="Failed to generate file")

class Controller:
    def __init__(self):
        ...
    
    def add_gram_pos(self, text):
        """Small helper to store a new gram positive bacteria."""
        # We retrieve the underlying data from the entry
        current_text = self.gram_p_entry.get()
        # We need to make sure its not empty before storing
        if text != "":
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
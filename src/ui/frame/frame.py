import tkinter as tk
from typing import TYPE_CHECKING

from ..palette.palette import Palette

if TYPE_CHECKING:
    from ...controller.controller import Controller


class GramFrame(tk.Frame):
    def __init__(
        self, master: tk.Tk, name: str, entry_text: str, controller: Controller
    ):
        """
        The Frame class to represent the Bacteria entry widgets.
        The logic for both types is shared so we create a base class that can be
        used to extent both.

        Args:
            master is the root Tkinter application
            name is the name of the frame type (ie Gram Positive or Gram Negative)
            entry_text is the example text used for each entry (ie "Example: S aureus")
            controller is the main API for producing the generated Excel files
        """
        super().__init__(
            master=master,
            highlightbackground=Palette.HIGHLIGHT,
            highlightthickness=2,
            bg=Palette.FRAME_BG,
        )
        self.controller = controller
        self.name = name
        self.entry_text = entry_text
        # We configure the columns to make a nicer looking application
        self.columnconfigure(1, weight=1)
        # We then run the helper method to create our frame
        self._create_frame()

    def _create_frame(self):
        # We create the main label for our widget to inform our user about the type
        # of bacteria
        self.label = tk.Label(
            self,
            text=self.name,
            bg=self["bg"],
            fg=Palette.TEXT_FG,
            font=("Arial", 14, "bold"),
        )
        # We place it in the first row and column and have it span across columns
        self.label.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        # We then create our button for adding bacteria, the logic for which bacteria
        # is added is deferred to the runtime of the application inside the Controller
        # class
        self.add = tk.Button(
            self,
            text="Add New Bacteria",
            command=lambda: self.controller.add_bacteria(
                self.name, self.entry, self.entry_label
            ),
            bg=Palette.BUTTON_BG,
            fg=Palette.BUTTON_FG,
            activebackground=Palette.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=5,
        )
        # We then place the button in the next row and have it expand towards the
        # left of the screen with a bit of padding
        self.add.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="W")

        # We can then create the entry for where our users provide the bacteria
        # type
        self.entry = tk.Entry(
            self, bg=Palette.ENTRY_BG, fg=Palette.ENTRY_FG, relief="flat"
        )
        # We place it in the same row as the button but in the column to the right
        # We also add padding and make it stick the left
        self.entry.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="W")

        # Finally, we create the label to display the example text which
        # is updated after bacteria are submitted for processing
        self.entry_label = tk.Label(
            self,
            text=self.entry_text,
            wraplength=200,
            justify=tk.LEFT,
            bg=self["bg"],
            fg=Palette.TEXT_FG,
            font=("Arial", 10, "italic"),
        )
        # We place this weidget below the previous two, in the second column with
        # a bit of padding and have it stick to the left
        self.entry_label.grid(row=2, column=1, padx=(5, 10), pady=(0, 10), sticky="W")


class ControlFrame(tk.Frame):
    def __init__(self, master, controller: Controller):
        """
        The ControlFrame is the main frame for actually generating the random Excel
        file. As such, the Controller API is exposed the most to this class.

        Args:
            master is the root for the main Tkinter application
            controller is the Controller class instance
        """
        super().__init__(
            master=master,
            highlightbackground=Palette.HIGHLIGHT,
            highlightthickness=2,
            bg=Palette.FRAME_BG,
        )
        self.controller = controller
        # We configure the column to make the widget look nicer
        self.columnconfigure(1, weight=1)
        # We can then initialize each component using the helper functions
        # We create the basis for the frame
        self._create_frame()

        # We then add the widgets providing the main logic for the application
        self._create_sections_widget()
        self._create_students_widget()
        self._create_generate_widget()

    def _create_frame(self):
        self.label = tk.Label(
            self,
            text="Generate",
            bg=self["bg"],
            fg=Palette.TEXT_FG,
            font=("Arial", 14, "bold"),
        )
        self.label.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="W")

    def _create_sections_widget(self):
        self.show_sections = tk.Label(
            self,
            text="Please provide the number of sections",
            bg=Palette.FRAME_BG,
            fg=Palette.TEXT_FG,
            font=("Arial", 11, "bold"),
        )
        self.show_sections.grid(row=0, column=1, pady=(10, 2), padx=(0, 10), sticky="W")

        self.add_sections = tk.Button(
            self,
            text="Add number of sections",
            command=lambda: self.controller.add_section_number(
                self.add_section_entry, self.show_sections
            ),
            bg=Palette.BUTTON_BG,
            fg=Palette.BUTTON_FG,
            activebackground=Palette.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=5,
        )
        self.add_sections.grid(row=1, column=0, padx=(10, 5), pady=2, sticky="W")

        self.add_section_entry = tk.Entry(
            self, bg=Palette.ENTRY_BG, fg=Palette.ENTRY_FG, relief="flat"
        )
        self.add_section_entry.grid(row=1, column=1, padx=(0, 10), pady=2, sticky="EW")

    def _create_students_widget(self):
        # We need to do the same for the number of students per class
        self.count_label = tk.Label(
            self,
            text="Please provide number of students per class",
            bg=Palette.FRAME_BG,
            fg=Palette.TEXT_FG,
            font=("Arial", 11, "bold"),
        )
        self.count_label.grid(row=2, column=1, pady=(10, 2), padx=(0, 10), sticky="W")

        self.add_count = tk.Button(
            self,
            text="Add students per class",
            command=lambda: self.controller.add_student_number(
                self.student_count_entry, self.count_label
            ),
            bg=Palette.BUTTON_BG,
            fg=Palette.BUTTON_FG,
            activebackground=Palette.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=5,
        )
        self.add_count.grid(row=3, column=0, padx=(10, 5), pady=2, sticky="W")

        self.student_count_entry = tk.Entry(
            self, bg=Palette.ENTRY_BG, fg=Palette.ENTRY_FG, relief="flat"
        )
        self.student_count_entry.grid(
            row=3, column=1, padx=(0, 10), pady=2, sticky="EW"
        )

    def _create_generate_widget(self):
        self.file_name_label = tk.Label(
            self,
            text="Please provide the file name",
            bg=Palette.FRAME_BG,
            fg=Palette.TEXT_FG,
            font=("Arial", 11, "bold"),
        )
        self.file_name_label.grid(
            row=4, column=1, pady=(10, 2), padx=(0, 10), sticky="W"
        )

        self.add_file_name = tk.Button(
            self,
            text="Add the file name",
            command=lambda: self.controller.add_file_name(
                self.file_name_entry, self.file_name_label
            ),
            bg=Palette.HIGHLIGHT,
            fg=Palette.BUTTON_FG,
            activebackground=Palette.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=5,
        )
        self.add_file_name.grid(row=5, column=0, padx=(10, 5), pady=2, sticky="W")

        self.file_name_entry = tk.Entry(
            self, bg=Palette.ENTRY_BG, fg=Palette.ENTRY_FG, relief="flat"
        )
        self.file_name_entry.grid(row=5, column=1, padx=(0, 10), pady=2, sticky="EW")

        self.generate = tk.Button(
            self,
            text="Generate Random Bacteria",
            command=lambda: self.controller.generate_random(self.status),
            bg=Palette.HIGHLIGHT,
            fg=Palette.BUTTON_FG,
            activebackground=Palette.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=6,
        )
        self.generate.grid(row=6, column=0, padx=(10, 5), pady=15, sticky="W")

        self.status = tk.Label(
            self,
            text="Not generated",
            bg=Palette.FRAME_BG,
            fg=Palette.TEXT_FG,
            font=("Arial", 12, "bold"),
        )
        self.status.grid(row=6, column=1, sticky="W", padx=10, pady=15)

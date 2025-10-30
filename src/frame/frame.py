import tkinter as tk

from ..palette.palette import Palette

class GramFrame(tk.Frame):
    def __init__(self, master, name, entry_text):
        super().__init__(
            master=master,
            highlightbackground=Palette.HIGHLIGHT,
            highlightthickness=2,
            bg=Palette.FRAME_BG,
        )
        self.name = name
        self.entry_text = entry_text
        self.columnconfigure(1, weight=1)
        self._create_frame()

    def _create_frame(self):
        self.label = tk.Label(
            self,
            text=self.name,
            bg=self["bg"],
            fg=Palette.TEXT_FG,
            font=("Arial", 14, "bold"),
        )
        self.label.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        self.add = tk.Button(
            self,
            text="Add New Bacteria",
            command=lambda: print("Button click", self.name),
            bg=Palette.BUTTON_BG,
            fg=Palette.BUTTON_FG,
            activebackground=Palette.HIGHLIGHT,
            borderwidth=0,
            padx=10,
            pady=5,
        )
        self.add.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="W")

        self.entry = tk.Entry(
            self, bg=Palette.ENTRY_BG, fg=Palette.ENTRY_FG, relief="flat"
        )
        self.entry.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="W")

        self.entry_label = tk.Label(
            self,
            text=self.entry_text,
            wraplength=200,
            justify=tk.LEFT,
            bg=self["bg"],
            fg=Palette.TEXT_FG,
            font=("Arial", 10, "italic"),
        )
        self.entry_label.grid(row=2, column=1, padx=(5, 10), pady=(0, 10), sticky="W")


class ControlFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master=master,
            highlightbackground=Palette.HIGHLIGHT,
            highlightthickness=2,
            bg=Palette.FRAME_BG,
        )
        self.columnconfigure(1, weight=1)
        self._create_frame()
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
            command=lambda: print("Add sections."),
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
            command=lambda: print("Add number of students"),
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
        self.generate = tk.Button(
            self,
            text="Generate Random Bacteria",
            command=lambda: print("Generate"),
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
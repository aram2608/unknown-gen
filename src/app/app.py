import tkinter as tk
from ..ui.frame.frame import GramFrame, ControlFrame
from ..controller.controller import Controller
from ..ui.menu.menu import GramMenu

class App(tk.Tk):
    """
    Main class used to represent our application.
    This class inherits from the Tk base class and instead of taking parameters,
    is initialized with components for every new instance.
    """
    def __init__(self):
        """
        The App class initializer.
        No parameters are needed to create an App instance.
        """
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
        """Helper method to populate the app with the desired frames."""
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

    def __call__(self):
        """
        Operator overload for the () operator.
        This allows us to use the App instance as a callable.
        Example:
            app = App()
            app()
        """
        return self.mainloop()

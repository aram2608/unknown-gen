import tkinter as tk

# Playing with menus for better usability

root = tk.Tk()

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
edit_menu = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)

# File Commands
file_menu.add_command(label="New", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))
file_menu.add_command(label="About", command=lambda: print("About my awesome program"))
# Add a visual separator
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu commands
edit_menu.add_command(label="Cut", command=lambda: print("Cut"))
edit_menu.add_command(label="Copy", command=lambda: print("Copy"))
edit_menu.add_command(label="Paste", command=lambda: print("Paste"))

if __name__ == "__main__":
    root.mainloop()
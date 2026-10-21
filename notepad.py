import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Notepad")
root.geometry("500x400")

# Text area with scrollbar
text = tk.Text(root, wrap="word", undo=True)
scroll = tk.Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")
text.pack(fill="both", expand=True)

current_file = None

def new_file():
    global current_file
    text.delete("1.0", "end")
    current_file = None
    root.title("Notepad")

def open_file():
    global current_file
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if path:
        with open(path, "r") as f:
            text.delete("1.0", "end")
            text.insert("1.0", f.read())
        current_file = path
        root.title("Notepad - " + path)

def save_as():
    global current_file
    path = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if path:
        with open(path, "w") as f:
            f.write(text.get("1.0", "end-1c"))
        current_file = path
        root.title("Notepad - " + path)

def save_file():
    if current_file:
        with open(current_file, "w") as f:
            f.write(text.get("1.0", "end-1c"))
        messagebox.showinfo("Notepad", "File saved")
    else:
        save_as()

def exit_app():
    root.destroy()

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: text.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text.event_generate("<<Paste>>"))
edit_menu.add_command(label="Undo", command=lambda: text.edit_undo())
edit_menu.add_command(label="Select All", command=lambda: text.tag_add("sel", "1.0", "end"))

root.mainloop()

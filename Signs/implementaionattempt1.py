#5Hhg.py
#tried to make a signs interpriter by making a code editor

import tkinter as tk
from tkinter import *
from tkinter import filedialog
root = tk.Tk()
root.title=("Signs Interpriter")
root.geometry=('1000x500')
def whereopen():
    root.file_name = filedialog.askopenfilename(
        initialdir="your directory path",
        title="",
        filetypes=(("Signs files", ".sign")),
    )
    selected_file = __file__.open(root.file_name)
    selected_file = selected_file.resize((300, 205), Image.ANTIALIAS)
    root.file = Tk.image(selected_file)
    selected_file_label = Label(root, file=root.image).pack()
def wheresave():
    file = filedialog.asksaveasfile(
        defaultextension=".sign",
        filetypes=[
            ("Signs file", ".sign"),
        ],
    )
    if file is None:
        return
    filetext = str(file.get(1.0, END))
    file.write(filetext)
    file.close()
def exitcomp():
    print("Compiler closed. You can reopen the compiler")
    root.destroy()
    exit()
def you_sureqm():
    label = tk.Label(root, text="Are you sure you want to make a new file?\n(You have to open the aplication again\nsince i haven't made the feature)")
    label.pack()
    button = tk.Button(root, text="Yes", command=exitcomp)
    button.pack()
    root.mainloop()
button = tk.Button(text="NEW", command=you_sureqm)
button2 = tk.Button(text="SAVE", command=wheresave)
button3 = tk.Button(text="OPEN", command=whereopen)
button.pack()
button2.pack()
button3.pack()
entry = tk.Entry(root, show=None, width=50,)
entry.pack()
root.mainloop()
#Eso Program
def priority():
    print("Priority road")
def endpriority():
    print("End of priority road")

#3O93.py
#tried to make a signs interpriter by making a code editor

import tkinter as tk
from tkinter import *
from tkinter import filedialog
root = tk.Tk()
root.title=("Signs Interpriter")
root.geometry=('1000x500')
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
button.pack()
button2.pack()
entry = tk.Entry(root, show=None, width=50,)
entry.pack()
root.mainloop()
#Eso Program
def priority():
    print("Priority road")
def endpriority():
    print("End of priority road")

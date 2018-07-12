from tkinter import *
import tkinter.filedialog
root=Tk("Text Editor")
text=Text(root)
text.grid()
def saveas():
    global text
    t = text.get("1.0", END)
    savelocation=tkinter.filedialog.asksaveasfilename()
    filesave=open(savelocation,"w+")
button=Button(root, text="Save", command=saveas)
button.grid()
root.mainloop()

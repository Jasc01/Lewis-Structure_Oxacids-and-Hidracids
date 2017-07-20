from tkinter import *
import util as Util

'''
Crea un cuadro de diálogo, el cual se usa para alertar al usuario de algún evento especial
'''
def createDialog(parent, title, labelText):
    top = Toplevel(parent)
    top.transient(parent)
    top.grab_set()
    if len(title) > 0:
        top.title(title)
    Label(top, text=labelText, font=("", 15)).pack()
    top.bind("<Return>", ok)
    b = Button(top, text="OK", command=lambda: ok(top))
    b.pack(pady=5)
    Util.center(top)


def ok(top):
    top.destroy()
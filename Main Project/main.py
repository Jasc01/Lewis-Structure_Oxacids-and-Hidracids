# Se importan las librerías
import util as Util
import dialog as Dialog
import atom_creator as AtomCreator
import lewis_creator as LewisCreator
import lewis_painter as LewisPainter
import name_molecule as NameMolecule

from tkinter import filedialog
from tkinter import ttk
from tkinter import *

from turtle import *

#Global variables
MoleculesArray = []
root = Tk()
canvas = None
nextButton = None
labelMolecule = None
labelNameMolecule = None

'''
Crea la interfaz gráfica
Asigna las funciones correspondientes a los botones
'''
def main():
    global root, canvas, nextButton, labelMolecule, labelNameMolecule

    root.title("Estructura de Lewis")
    root.geometry("1024x720")
    root.resizable(width=False, height=False)
    Util.center(root)

    mainFrame = ttk.Frame(root, padding="20")
    fileButton = ttk.Button(mainFrame, text="Abrir archivo", command=openFile)
    nextButton = ttk.Button(mainFrame, text="Siguiente estructura", command=readMolecule)
    canvas = Canvas(mainFrame, width=790, height=500, bg="grey")
    labelMolecule = ttk.Label(mainFrame, font=("", 20))
    labelNameMolecule = ttk.Label(mainFrame, font=("", 20))
    fileButton.pack()
    labelMolecule.pack()
    canvas.pack()
    labelNameMolecule.pack()
    nextButton.pack()
    mainFrame.pack()
    root.mainloop()

'''
Abre un archivo txt desde un file chooser
Borrar espacio al final de cada nombre
'''
def openFile():
    global MoleculesArray
    filePath = filedialog.askopenfilename(filetypes=(("txt file", "*.txt"),("all files", "*.*")))
    if filePath != "":
        file = open(filePath, "r")
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            MoleculesArray.append(line)

'''
Valida las moléculas leídas del txt
Llama a la función que crea un Átomo
Llama a la función que crea moléculas
Llama a la función que dibuja moléculas
'''
def readMolecule():
    global MoleculesArray, canvas, nextButton, labelMolecule, labelNameMolecule
    canvas.delete("all")
    if len(MoleculesArray) == 0:
        Dialog.createDialog(root, "Alerta", "No hay moléculas por analizar")
    elif NameMolecule.nameMolecule(MoleculesArray[0]) == "":
        Dialog.createDialog(root, "Alerta", "La molécula es incorrecta")
        MoleculesArray = MoleculesArray[1:]
        labelMolecule.config(text="")
        labelNameMolecule.config(text="")
    else:
        labelMolecule.config(text=MoleculesArray[0])
        labelNameMolecule.config(text=NameMolecule.nameMolecule(MoleculesArray[0]))
        #print(MoleculesArray)
        arrayAtom = AtomCreator.createAtom(MoleculesArray[0]) #Index 0 because the list is gonna shrink one by one
        #Call lewis_creator
        resultMolecule = LewisCreator.createLewis(arrayAtom)
        #Call painter
        nextButton.config(state=DISABLED)
        LewisPainter.drawLewis(canvas, resultMolecule, 180, 0, 0, 0, True)
        nextButton.config(state=NORMAL)
        MoleculesArray = MoleculesArray[1:]

main()
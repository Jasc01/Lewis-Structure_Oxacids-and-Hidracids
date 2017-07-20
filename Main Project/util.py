'''
Centrar pantalla
'''
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

'''
Busca si hay un átomo en una array de átomos, por nombre
'''
def checkAtomInArrayByName(arrayAtoms, name):
    for atom in arrayAtoms:
        if atom.name == name:
            return True
    return False

'''
Imprime un átomo
'''
def printAtom(atom, identNum):
    ident = " " * identNum
    print(ident + "Name: " + atom.name)
    print(ident + "Quantity: " + str(atom.quantity))
    print(ident + "Real Bonds: " + str(atom.Bonds))
    print(ident + "Single Dots: " + str(atom.singleDots))
    print(ident + "Double Dots: " + str(atom.doubleDots))
    print(ident + "List of Bonded Atoms: ")
    if len(atom.arrayAtoms) == 0:
        print(ident + "NO BONDED ATOMS")
    else:
        for bondedAtom in atom.arrayAtoms:
            printAtom(bondedAtom, identNum + 3)

# def sortByElectroNeg(arrayAtoms):
#     for i in range(len(arrayAtoms)-1, 0, -1):
#         for j in range(i):
#             if arrayAtoms[j].electroNeg > arrayAtoms[j+1].electroNeg:
#                 temp = arrayAtoms[j]
#                 arrayAtoms[j] = arrayAtoms[j+1]
#                 arrayAtoms[j+1] = temp
#     return arrayAtoms
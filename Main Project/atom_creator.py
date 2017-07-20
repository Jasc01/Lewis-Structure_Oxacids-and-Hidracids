import atom as Atom

#Array para contar la electronegatividad
arrayElectroNeg = ["Mn", "Cr", "B", "Se", "S", "I", "Br", "N", "Cl", "O", "F", "H"] #H is the max because is never a central atom

'''
Busca un patró en el string que le llega
Básicamente, divide el string, en los elementos (por ejemplo, H, Cl, Cr)
Y si vienen números, entonces en el Atom está el atributo "quantity", el cual cambia de acuerdo a este número.
'''
def createAtom(strAtom):
    atomArray = []
    tempAtom = None
    for i in range(len(strAtom)):
        if strAtom[i].isupper():
            try:
                if strAtom[i+1].islower():
                    name = strAtom[i] + strAtom[i+1]
                else:
                    name = strAtom[i]
            except IndexError:
                name = strAtom[i]
            tempAtom = Atom.Atom(name, getElectroNegativity(name), getDoubleDots(name), getSingleDots(name))
            try:
                if not strAtom[i+1].isdigit():
                    atomArray.append(tempAtom)
            except IndexError:
                atomArray.append(tempAtom)
        else:
            if strAtom[i].isdigit():
                tempAtom.quantity = int(strAtom[i])
                atomArray.append(tempAtom)
    return atomArray

def getElectroNegativity(name):
    return arrayElectroNeg.index(name)

'''
Obtiene la cantidad de pares de electrones de valencia
'''
def getDoubleDots(name):
    #Switch - case for double dots in Elements
    if name == "H" or name == "B": return 0
    elif name == "N": return 1
    elif name == "O" or name == "S" or name == "Se" or name == "Cr": return 2
    elif name == "Cl" or name == "F" or name == "I" or name == "Br" or name == "Mn": return 3

'''
Obtiene la cantidad de electrones de valencia sueltos
'''
def getSingleDots(name):
    #Switch - case for single dots in Elements
    if name == "H": return 1
    elif name == "N" or name == "B": return 3
    elif name == "O" or name == "S" or name == "Se" or name == "Cr": return 2
    elif name == "Cl" or name == "F" or name == "I" or name == "Br" or name == "Mn": return 1
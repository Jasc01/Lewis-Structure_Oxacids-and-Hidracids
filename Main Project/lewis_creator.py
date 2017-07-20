import util as Util
import atom as Atom

centralAtom = None

'''
Principal creador de la parte lógica del progama
Básicamente, selecciona un elemento central de acuerdo a la electronegatividad
y luego crea un ÁRBOL de átomos, el cual empieza desde el elemento centra,
luego tiene los hidrógenos en el caso de los hidrácidos, y oxígenos en el caso de los
oxácidos
'''
def createLewis(arrayAtoms):
    global centralAtom
    centralAtom = getCentralAtom(arrayAtoms)
    ###Create all Hidracids and Oxacids (with one Center - To Do: two Centers)
    createMolecule(arrayAtoms)
    centralAtom.freeSpaces = len(centralAtom.arrayAtoms) if len(centralAtom.arrayAtoms) > 4 else 4
    Util.printAtom(centralAtom, 0)
    return centralAtom

'''
Obtiene el átomo central de acuerdo a la electronegatividad
'''
def getCentralAtom(arrayAtoms):
    tempAtom = arrayAtoms[0]
    lessNumber = arrayAtoms[0].electroNeg
    for atom in arrayAtoms:
        if atom.electroNeg < lessNumber:
            lessNumber = atom.electroNeg
            tempAtom = atom
    return tempAtom

'''
Crear la molécula agragando los oxígenos y los hidrógenos
Luego crea los enlaces, primero los simples, y luego implementa
los dobles en el caso que se pueda
'''
def createMolecule(arrayAtoms):
    global centralAtom
    arrayAtoms.remove(centralAtom)
    if addOxigenAtoms(arrayAtoms):
        arrayAtoms = removeOxigenAtoms(arrayAtoms)
    addHidrogenAtoms(arrayAtoms)
    addBonds(centralAtom) #The global variable is an argument because it's gonna iterate over itself (Recursivity)
    tryDoubleBonds()

'''
Agrega los átomos de oxígeno si hay
'''
def addOxigenAtoms(arrayAtoms):
    global centralAtom
    thereIs = False
    for atom in arrayAtoms:
        if atom.name == "O":
            thereIs = True
            for i in range(atom.quantity):
                tempAtom = Atom.Atom(atom.name, atom.electroNeg, atom.doubleDots, atom.singleDots)
                tempAtom.quantity = 1 #One atom can bound with one atom and no more
                centralAtom.arrayAtoms.append(tempAtom)
    return thereIs

'''
Quita los átomos de oxígeno en el caso que hayan
'''
def removeOxigenAtoms(arrayAtoms):
    return arrayAtoms[:-1] #This is gonna work if and only if the H comes former than the O

'''
Agrega los átomos de hidrogeno
'''
def addHidrogenAtoms(arrayAtoms):
    global centralAtom
    for i in range(arrayAtoms[0].quantity): #In Oxacids there's never more H than O
        tempAtom = Atom.Atom(arrayAtoms[0].name, arrayAtoms[0].electroNeg, arrayAtoms[0].doubleDots, arrayAtoms[0].singleDots)
        tempAtom.quantity = 1 #One atom can bound with one atom and no more
        if Util.checkAtomInArrayByName(centralAtom.arrayAtoms, "O"):
            centralAtom.arrayAtoms[i].arrayAtoms.append(tempAtom)
        else:
            centralAtom.arrayAtoms.append(tempAtom)

'''
Crea los enlaces simples entre los átomos que están juntos (o sea, que están conectados 
directamente en el árbol)
'''
def addBonds(pAtom):
    subAtomsQuantity = len(pAtom.arrayAtoms)
    while subAtomsQuantity > 0:
        if pAtom.singleDots > 0:
            pAtom.Bonds.append("SINGLE")
            pAtom.singleDots -= 1
            pAtom.arrayAtoms[subAtomsQuantity - 1].singleDots -= 1
            subAtomsQuantity -= 1
            addBonds(pAtom.arrayAtoms[subAtomsQuantity - 1])
        elif pAtom.doubleDots > 0:
            pAtom.doubleDots -= 1
            pAtom.singleDots += 2
    return

'''
Crea enlaces dobles cuando se puede
'''
def tryDoubleBonds():
    global centralAtom
    if centralAtom.singleDots > 0 or centralAtom.doubleDots > 0:
        subAtomsQuantity = len(centralAtom.arrayAtoms)
        while subAtomsQuantity > 0:
            if centralAtom.arrayAtoms[subAtomsQuantity - 1].singleDots > 0:
                if centralAtom.singleDots > 0:
                    centralAtom.singleDots -= 1
                    centralAtom.arrayAtoms[subAtomsQuantity - 1].singleDots -= 1
                    centralAtom.Bonds[subAtomsQuantity - 1] = "DOUBLE"
                    subAtomsQuantity -= 1
                elif centralAtom.doubleDots > 0:
                    centralAtom.doubleDots -= 1
                    centralAtom.singleDots += 2
            else:
                subAtomsQuantity -= 1



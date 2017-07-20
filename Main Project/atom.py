'''
Clase que se comporta como estructura para guardar un átomo, y los
diferentes atributos que tiene
'''
class Atom:
    def __init__(self, name, electroNeg, doubleDots, singleDots):
        self.name = name
        self.quantity = 1
        self.electroNeg = electroNeg

        self.arrayAtoms = []
        self.Bonds = []

        self.doubleDots = doubleDots
        self.singleDots = singleDots

        #for drawing
        self.freeSpaces = 4
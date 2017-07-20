import turtle
from math import *

'''
Constantes que definen aspectos de diseño
'''
FONT_SIZE = "20"
RADIOUS_SIZE_WORD = 16 #Related to font_size
RADIOUS_SIZE_GENERAL = 22
DOT_SIZE = 4
SPACE_BETWEEN_LINES = 18
LINE_SIZE = 50
SPACE_BETWEEN_DOUBLES = 4

'''
Función que llama a la función recursiva para dibujar
Incializa un lápiz para dibujar, lo esconde, y lo hace inmediato con la velocidad en 0
'''
def drawLewis(canvas, pMolecule, forbiddenAngle, angle, originalX, originalY, isFirst):
    turtlePainter = turtle.RawTurtle(canvas)
    turtlePainter.hideturtle()
    turtlePainter.speed(0)
    drawLewisAux(canvas, turtlePainter, pMolecule, forbiddenAngle, angle, originalX, originalY, isFirst)

'''
Dibuja la molécula
Cuida la simetría con algunas características, principalmente 
modificando los ángulos de los círculos imaginarios que tiene cada Letra
Es recursiva, primero dibuja los elances (ya sean simples o dobles),
luego los puntos simples (creo que no hay ningún ejemplo en el que pasa esto, pero por si acaso),
y luego los puntos dobles
Básicamente, dibuja una Letra, luego le hace un círculo imaginario, el cual divide en ángulos de acuerdo a lo que
necesito dividir. Luego empieza a dibujar elementos en esos ángulos.
Luego se llama a sí misma (recursividad), pero con la siguiente Letra
'''
def drawLewisAux(canvas, turtlePainter, pMolecule, forbiddenAngle, angle, originalX, originalY, isFirst):
    runWordTurtle(turtlePainter, pMolecule.name, originalX, originalY)
    #print("Dibujé Letra")
    angleDivisor = 360 // pMolecule.freeSpaces
    originalAngle = angle
    needSymmetryFix = False
    for i in range(len(pMolecule.Bonds)):
        if (not isFirst) and (angle == forbiddenAngle):
            angle += angleDivisor
        #Draw Bonds
        if pMolecule.Bonds[i] == "SINGLE":
            runSingleLineTurtle(turtlePainter, angle, originalX, originalY)
            #print("Dibujé Línea")
        else:
            runDoubleLineTurtle(turtlePainter, angle, originalX, originalY)
            #print("Dibujé Doble Línea")
            needSymmetryFix = True

        forbiddenAngle = angle + 180
        if needSymmetryFix:
            angleToSend = angle + 90
        else:
            angleToSend = angle
        drawLewisAux(canvas, turtlePainter, pMolecule.arrayAtoms[i], forbiddenAngle, angleToSend, turtlePainter.xcor(), turtlePainter.ycor(), False)
        if angle == originalAngle + 180:
            angle = originalAngle + angleDivisor
            originalAngle = angle
        else:
            angle = angle + 180
    #Draw Single Dot
    for i in range(pMolecule.singleDots):
        if (not isFirst) and (angle == forbiddenAngle):
            angle += angleDivisor
        runSingleDotTurtle(turtlePainter, angle, originalX, originalY)
        #print("Dibujé Punto")
        if angle == originalAngle + 180:
            angle = originalAngle + angleDivisor
            originalAngle = angle
        else:
            angle = angle + 180
    #Draw Double Dots
    for i in range(pMolecule.doubleDots):
        if (not isFirst) and (angle == forbiddenAngle):
            angle += angleDivisor
        runDoubleDotTurtle(turtlePainter, angle, originalX, originalY)
        #print("Dibujé Doble Punto")
        if angle == originalAngle + 180:
            angle = originalAngle + angleDivisor
            originalAngle = angle
        else:
            angle = angle + 180

'''
Se usa para cambiar la positión del lápiz
'''
def changePenPosition(pTurtle, xPoint, yPoint):
    pTurtle.penup()
    pTurtle.setx(xPoint)
    pTurtle.sety(yPoint)
    pTurtle.pendown()

'''
Se usa para cambiar la posición del lápiz en el círculo imaginario de acuerdo al ángulo
'''
def changeAngularPosition(pTurtle, angle, originalX, originalY):
    pTurtle.seth(angle)
    lineX = originalX + RADIOUS_SIZE_GENERAL * cos(radians(angle))
    lineY = originalY + RADIOUS_SIZE_GENERAL * sin(radians(angle))
    changePenPosition(pTurtle, lineX, lineY)
    return [lineX, lineY]

'''
Dibuja una línea recta en un ángulo y lugar definido
'''
def runSingleLineTurtle(pTurtle, angle, originalX, originalY):
    changeAngularPosition(pTurtle, angle, originalX, originalY)
    pTurtle.forward(LINE_SIZE)
    pTurtle.penup()
    pTurtle.forward(SPACE_BETWEEN_LINES)
    pTurtle.pendown()

'''
Dibuja una doble línea en un ángulo y lugar definido
Para esto, levanta el lápiz, se mueve, baja el lápiz, dibuja, vuelve a su posición central,
levanta, mueve, baja, dibuja de nuevo, y vuelve a la central
'''
def runDoubleLineTurtle(pTurtle, angle, originalX, originalY):
    angularPosition = changeAngularPosition(pTurtle, angle, originalX, originalY)
    pTurtle.penup()
    pTurtle.seth(angle - 90)
    pTurtle.forward(SPACE_BETWEEN_DOUBLES)
    pTurtle.seth(angle)
    pTurtle.pendown()
    pTurtle.forward(LINE_SIZE)
    changePenPosition(pTurtle, angularPosition[0], angularPosition[1])
    pTurtle.penup()
    pTurtle.seth(angle + 90)
    pTurtle.forward(SPACE_BETWEEN_DOUBLES)
    pTurtle.seth(angle)
    pTurtle.pendown()
    pTurtle.forward(LINE_SIZE)
    changePenPosition(pTurtle, angularPosition[0], angularPosition[1])
    pTurtle.penup()
    pTurtle.forward(LINE_SIZE + SPACE_BETWEEN_LINES)
    pTurtle.pendown()

'''
Dibuja un punto en un lugar específico
'''
def runSingleDotTurtle(pTurtle, angle, originalX, originalY):
    changeAngularPosition(pTurtle, angle, originalX, originalY)
    pTurtle.dot(DOT_SIZE)

'''
Dibuja un par de puntos en un ángulo y lugar específico
'''
def runDoubleDotTurtle(pTurtle, angle, originalX, originalY):
    angularPosition = changeAngularPosition(pTurtle, angle, originalX, originalY)
    pTurtle.penup()
    pTurtle.seth(angle - 90)
    pTurtle.forward(SPACE_BETWEEN_DOUBLES)
    pTurtle.seth(angle)
    pTurtle.pendown()
    pTurtle.dot(DOT_SIZE)
    changePenPosition(pTurtle, angularPosition[0], angularPosition[1])
    pTurtle.penup()
    pTurtle.seth(angle + 90)
    pTurtle.forward(SPACE_BETWEEN_DOUBLES)
    pTurtle.seth(angle)
    pTurtle.pendown()
    pTurtle.dot(DOT_SIZE)
    changePenPosition(pTurtle, angularPosition[0], angularPosition[1])

'''
Dibuja una Letra en un lugar en específico, y siempre lo hace en 270 grados,
ya que así está recta hacia la vista
'''
def runWordTurtle(pTurtle, pWord, originalX, originalY):
    wordX = originalX + RADIOUS_SIZE_WORD * cos(radians(270))
    wordY = originalY + RADIOUS_SIZE_WORD * sin(radians(270))
    changePenPosition(pTurtle, wordX, wordY)
    pTurtle.write(pWord, align="center", font=("", FONT_SIZE, ""))
    changePenPosition(pTurtle, originalX, originalY)
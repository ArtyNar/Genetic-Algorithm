from LineList import LineList
from random import uniform
from math import sin, cos, pi
import tkinter 

class Line:
    # Constructor
    def __init__(self, x , y, length, angle):
        self.length = length
        self.angle = angle
        self.x = x
        self.y = y

    def __str__(self):
        return ("x=%d y=%d" % (self.x, self.y))

def genFullLine(x, y, numLines):
    line = LineList()
    for each in range(numLines):
        angl = uniform(-pi/2, pi/2)
        len = uniform(5, 20)

        line.insert(data=Line(x, y, angle=angl, length=len))
        x = x - len * sin(angl)
        y = y - len * cos(angl)
    return line

def drawLine(fullLine):
    top = tkinter.Tk()
    for line in fullLine:
        C = tkinter.Canvas(top, height=500, width=500)

        C.create_line(line.x, line.y, line.length, line.angle)
    C.pack()
    top.mainloop()


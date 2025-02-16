#TurtleGraphics.py
#Name: Jessica Pusher
#Date: 2/16/25
#Assignment: turtle

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(jane, size):
    for i in range(4):
        jane.forward(size)
        jane.right(90)
        
def drawPolygon(jane, sides):
    for s in range(sides):
        jane.forward(50)
        jane.right(360/sides)
        
def fillCorner(jane, corner):
    #draw big square
    jane.goto(0, 0)
    drawSquare(jane, 100)
    
    #draw small square
    def drawSmallSquare (jane):
        jane.begin_fill()
        drawSquare(jane, 50)
        jane.end_fill()
    
    if corner == 1:
        jane.goto (0.0)
        drawSmallSquare (jane)
    elif corner == 2:
        jane.goto (50, 0)
        drawSmallSquare (jane)
    elif corner == 3:
        jane.goto (0, -50)
        drawSmallSquare (jane)
    elif corner == 4:
        jane.up()
        jane.goto (50, -50)
        jane.down()
        drawSmallSquare (jane)
        
def squaresInSquares(jane, number):
    x = -1
    y = 1
    size = 10
    for t in range(number):
        while number > 0:
            jane.up()
            jane.goto (x, y)
            jane.down()
            drawSquare(jane, size)
            size = (size + 10)
            x = (x - 5)
            y = (y + 5)
            number = (number - 1)
    

def main():
    jane = turtle.Turtle()
    
    #drawSquare(jane, 100)
    
    #drawPolygon(jane, 5) #draws a pentagon
    #drawPolygon(jane, 8) #draws an octogon

    #fillCorner(jane, 2) #draws a square with top right corner filled in.
    #fillCorner(jane, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(jane, 5) #draws 5 concentric squares
    #squaresInSquares(jane, 3) #draws 3 concentric squares


main()

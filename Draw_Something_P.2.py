import turtle
import os


def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    t.begin_fill()
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)
    t.end_fill()

def drawFilledCircle(anyTurtle, radius,color):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    anyTurtle.fillcolor(color)
    anyTurtle.up()
    anyTurtle.forward(radius)
    anyTurtle.left(90)
    anyTurtle.down()
    drawFilledPolygon(anyTurtle, sideLength, 360)


def drawWFilledCircle(anyTurtle, radius,color):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    anyTurtle.fillcolor(color)
    drawFilledPolygon(anyTurtle, sideLength, 360)


def drawFilledPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    t.begin_fill()
    for i in range(numSides):
        t.forward(sideLength)
        t.left(turnAngle)
    t.end_fill()

def drawThreeQuarterFilledCircle(anyTurtle, radius,fillcolor,outlinecolor):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    anyTurtle.color(outlinecolor,fillcolor)
    anyTurtle.up()
    anyTurtle.forward(radius)
    anyTurtle.left(90)
    anyTurtle.down()
    drawTQFilledPolygon(anyTurtle, sideLength, 360)


def drawTQFilledPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    t.begin_fill()
    for i in range(3*numSides/4):
        t.forward(sideLength)
        t.lt(turnAngle)
    t.end_fill()

def BackTOREC():
    head.up()
    head.home()
    head.lt(90)
    head.fd(50)
    head.lt(180)
    head.fd(50)
    head.lt(90)
    head.fd(30)
    head.rt(90)
    head.down()


#Photoshop Colors
NEON_YELLOW = "#f5ed09"
BLACK = "#ebd30c"
W = "#ffffff"
SHADE = "#ad9f28"
SKY ="#01fef5"

#Background Character initialization
shape = turtle.Turtle()
shape2 = turtle.Turtle()
shape3 = turtle.Turtle()
shape4  = turtle.Turtle()
shape5 = turtle.Turtle()
shape6 = turtle.Turtle()
shape7 = turtle.Turtle()
for n in (shape,shape3,shape2,shape4,shape5,shape6,shape7):
    n.speed(0)
wn = turtle.Screen()
wn.bgcolor(SKY)
wn.screensize(400,400)
wn.colormode(255)
#Characters
wn.addshape(os.path.expanduser("Mario.gif"))
shape.shape(os.path.expanduser("Mario.gif"))
wn.addshape(os.path.expanduser("Luigi.gif"))
shape2.shape(os.path.expanduser("Luigi.gif"))
wn.addshape(os.path.expanduser("Peach.gif"))
shape3.shape(os.path.expanduser("Peach.gif"))
wn.addshape(os.path.expanduser("Yoshi2.gif"))
shape4.shape(os.path.expanduser("Yoshi2.gif"))
wn.addshape(os.path.expanduser("Toads.gif"))
shape5.shape(os.path.expanduser("Toads.gif"))
wn.addshape(os.path.expanduser("Rosalina.gif"))
shape6.shape(os.path.expanduser("Rosalina.gif"))
wn.addshape(os.path.expanduser("clouds.gif"))
shape7.shape(os.path.expanduser("clouds.gif"))

#background Characters
shape.up()
shape.goto(-400,400)

shape2.up()
shape2.goto(400,400)

shape3.up()
shape3.goto(-400,-400)

shape4.up()
shape4.goto(400,-400)

shape5.up()
shape5.goto(0,-400)

shape6.up()
shape6.goto(0,400)

shape7.up()
shape7.goto(400,0)
shape7.stamp()
shape7.goto(-400,0)

#turtle initaition/tracer
head = turtle.Turtle()
head.speed(0)
head.tracer(1000)


#yellow block
head.color(BLACK,NEON_YELLOW)
head.up()
head.fd(200)
head.left(90)
head.fd(200)
head.left(180)
head.down()
head.begin_fill()
for i in range (4):
    head.fd(400)
    head.right(90)
head.end_fill()

#top right black outercircle
head.up()
head.home()
head.fd(180)
head.left(90)
head.fd(170)
head.left(180)
head.down()
head.color('black',SHADE)
drawCircle(head, 20)

#top right black innercircle
head.up()
head.home()
head.fd(180)
head.left(90)
head.fd(170)
head.left(180)
head.down()
head.color('black')
drawCircle(head, 15)

#bottom right black outercircle
head.up()
head.home()
head.fd(180)
head.left(90)
head.fd(180)
head.left(180)
head.forward(350)
head.down()
head.color('black',SHADE)
drawCircle(head, 20)

#bottom right black innercircle
head.up()
head.home()
head.fd(180)
head.left(90)
head.fd(180)
head.left(180)
head.forward(350)
head.down()
head.color('black')
drawCircle(head, 15)

#top left black outercircle
head.up()
head.home()
head.left(180)
head.fd(140)
head.rt(90)
head.fd(170)
head.left(180)
head.down()
head.color('black',SHADE)
drawCircle(head, 20)

#top left black innercircle
head.up()
head.home()
head.left(180)
head.fd(140)
head.rt(90)
head.fd(170)
head.left(180)
head.down()
head.color('black')
drawCircle(head, 15)

#bottom left black outercircle
head.up()
head.home()
head.left(180)
head.fd(140)
head.rt(90)
head.fd(180)
head.left(180)
head.forward(350)
head.down()
head.color('black',SHADE)
drawCircle(head, 20)

#bottom left black innercircle
head.up()
head.home()
head.left(180)
head.fd(140)
head.rt(90)
head.fd(180)
head.left(180)
head.forward(350)
head.down()
head.color('black')
drawCircle(head, 15)

#top part of question mark(big circle)
head.up()
head.home()
head.lt(90)
head.fd(50)
head.lt(180)
drawThreeQuarterFilledCircle(head,100,W,W)

#carve out circle in middle of question mark
head.home()
head.lt(90)
head.fd(50)
head.lt(180)
drawThreeQuarterFilledCircle(head,50,NEON_YELLOW,NEON_YELLOW)

#deleting extra white from top part of question mark
head.home()
head.lt(90)
head.fd(50)
head.lt(90)
head.color(NEON_YELLOW,NEON_YELLOW)
head.begin_fill()
for n in range (4):
    head.fd(100)
    head.lt(90)
head.end_fill()

#middle part(the rectangle) of question mark
BackTOREC()
head.color(W,W)
head.begin_fill()
for s in range(2):
    head.fd(120)
    head.rt(90)
    head.fd(50)
    head.rt(90)
head.end_fill()


#Lower part of question mark(the small circle)
head.up()
head.home()
head.right(90)
head.fd(160)
head.left(90)
head.forward(8)
drawFilledCircle(head,30,'White')

#tracer ending
head.up()
head.color("black","black")
head.goto(-1000,1000)
for z in range(10000):
    head.forward(1)

wn.exitonclick()
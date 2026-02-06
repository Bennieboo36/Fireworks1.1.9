# import turtle and math
import turtle
import math

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

# draw the colored lines for firework 1
for i in range(360):
    # alternate colors
    if i % 2 == 0:
        t.pencolor("purple")
    else:
        t.pencolor("white")
    
    # mathematical drawing
    t.penup()
    t.goto(-200,275)
    dist = math.sin(math.radians(i * 5)) * 130
    t.pendown()
    t.forward(dist)
    t.left(59)
    # return to center of firework without drawing
    t.penup()
    t.goto(-200,275)
    t.pendown()

# draw the colored lines for firework 2
for i in range(360):
    # alternate colors
    if i % 2 == 0:
        t.pencolor("lightgreen")
    else:
        t.pencolor("white")
    
    # mathematical drawing
    t.penup()
    t.goto(25,190)
    dist = math.sin(math.radians(i * 5)) * 100
    t.pendown()
    t.forward(dist)
    t.left(59)
    # return to center of firework without drawing
    t.penup()
    t.goto(25,190)
    t.pendown()

# draw the colored lines for firework 3
for i in range(360):
    # alternate colors
    if i % 2 == 0:
        t.pencolor("pink")
    else:
        t.pencolor("white")
    
    # mathematical drawing
    t.penup()
    t.goto(300,250)
    dist = math.sin(math.radians(i * 5)) * 200
    t.pendown()
    t.forward(dist)
    t.left(59)
    # return to center of firework without drawing
    t.penup()
    t.goto(300,250)
    t.pendown()

# draw the colored lines for firework 4
for i in range(360):
    # alternate colors
    if i % 2 == 0:
        t.pencolor("yellow")
    else:
        t.pencolor("white")
    
    # mathematical drawing
    t.penup()
    t.goto(-275,170)
    dist = math.sin(math.radians(i * 5)) * 80
    t.pendown()
    t.forward(dist)
    t.left(59)
    # return to center of firework without drawing
    t.penup()
    t.goto(-275,170)
    t.pendown()

# draw grass
t.penup()
t.goto(-600,-100)
t.pendown()
t.fillcolor("green")
t.begin_fill()
for count in range(2):
    t.forward(1200)
    t.right(90)
    t.forward(400)
    t.right(90)
t.end_fill()

turtle.done()
# import turtle and math
import turtle
import math
import time


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
    t.goto(-400,170)
    dist = math.sin(math.radians(i * 5)) * 80
    t.pendown()
    t.forward(dist)
    t.left(59)
    # return to center of firework without drawing
    t.penup()
    t.goto(-400,170)
    t.pendown()

# draw grass
t.penup()
t.goto(-600,-100)
t.pendown()
t.fillcolor("darkgreen")
t.begin_fill()
for count in range(2):
    t.forward(1200)
    t.right(90)
    t.forward(400)
    t.right(90)
t.end_fill()

# add couple on grass
wn = turtle.Screen()
people_image = "People sitting.gif"
wn.addshape(people_image)
people = turtle.Turtle()
people.shape(people_image)
people.penup()
people.goto(0,-100)
people.pendown()

# draw infinite loop of fuses animation
# make new turtle so fireworks and grass don't clear when fuses clear
fuse = turtle.Turtle()
fuse.hideturtle()
fuse.speed(0)

while True: 
    # firework and fuse 1
    fuse.penup()
    fuse.goto(-200, -100)
    fuse.setheading(90)
    for d in range(-100, 275, 15):
        fuse.pencolor("purple" if (d//15)%2==0 else "white")
        fuse.pendown()
        fuse.forward(10)
        fuse.penup()
        fuse.forward(5)
        wn.update()
        time.sleep(0.01)
    fuse.clear() 

    # firework fuse 2
    fuse.penup()
    fuse.goto(25, -100)
    fuse.setheading(90)
    for d in range(-100, 195, 15):
        fuse.pencolor("lightgreen" if (d//15)%2==0 else "white")
        fuse.pendown()
        fuse.forward(10)
        fuse.penup()
        fuse.forward(5)
        wn.update()
        time.sleep(0.01)
    fuse.clear()

    # firework fuse 3
    fuse.penup()
    fuse.goto(300, -100)
    fuse.setheading(90)
    for d in range(-100, 250, 15):
        fuse.pencolor("pink" if (d//15)%2==0 else "white")
        fuse.pendown()
        fuse.forward(10)
        fuse.penup()
        fuse.forward(5)
        wn.update()
        time.sleep(0.01)
    fuse.clear()

    # firework fuse 4
    fuse.penup()
    fuse.goto(-400, -100)
    fuse.setheading(90)
    for d in range(-100, 170, 15):
        fuse.pencolor("yellow" if (d//15)%2==0 else "white")
        fuse.pendown()
        fuse.forward(10)
        fuse.penup()
        fuse.forward(5)
        wn.update()
        time.sleep(0.01)
    fuse.clear()

wn = turtle.Screen()
wn.mainloop()
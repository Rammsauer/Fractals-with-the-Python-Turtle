import turtle
from random import randint

turtle.speed(0)

def run():
    for x in range(72):
        tup = (0.25, 0.25, 0.5)
        turtle.pencolor(tup)

        turtle.circle(57.5)
        turtle.up()
        turtle.left(90)
        turtle.forward(114)
        turtle.left(270)
        turtle.down()

        tup = (0.5, 0.5, 0.75)
        turtle.pencolor(tup)

        turtle.circle(36)
        turtle.up()
        turtle.left(90)
        turtle.forward(71)
        turtle.left(270)
        turtle.down()

        tup = (0.25, 0.75, 1)
        turtle.pencolor(tup)

        turtle.circle(15.5)
        turtle.up()
        turtle.left(270)
        turtle.forward(185)
        turtle.left(90)
        turtle.down()

        turtle.left(355)


run()

turtle.getscreen()._root.mainloop()

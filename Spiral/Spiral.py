import turtle
from random import randint

turtle.speed(0)

def run():
    for x in range(750):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)

        tup = (r/256, g/256, b/256)
        turtle.pencolor(tup)

        turtle.forward(25 + x)
        turtle.left(90.911)


run()

turtle.getscreen()._root.mainloop()

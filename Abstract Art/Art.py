import turtle
from random import randint

def w():
    while True:
        turtle.forward(3)
        if (turtle.xcor() > 200) or (turtle.xcor() < -200) or (turtle.ycor() > 200) or (turtle.ycor() < -200):
            turtle.left(randint(90, 180))


w()

turtle.getscreen()._root.mainloop()

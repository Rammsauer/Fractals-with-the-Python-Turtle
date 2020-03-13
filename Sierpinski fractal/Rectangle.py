import turtle

l = 600

def rec(l):
    if l > 20:
        for i in range(3):
            rec(l/2)
            turtle.forward(l)
            turtle.right(120)

turtle.penup()
turtle.goto(-200, 180)
turtle.pendown()
rec(l)

turtle.getscreen()._root.mainloop()
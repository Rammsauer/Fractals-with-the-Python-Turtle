import turtle

def rec(length):
    for x in range(4):
        turtle.forward(length)
        turtle.left(90)

l = 5

for x in range(60):
    rec(l)
    turtle.left(7.5)
    l = l + 5


turtle.getscreen()._root.mainloop()
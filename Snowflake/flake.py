import turtle, math

def a1(l):
    turtle.forward(l)
    turtle.left(300)
    turtle.forward(l)
    turtle.left(120)
    turtle.forward(l)
    turtle.left(300)
    turtle.forward(l)
    turtle.left(120)

def a2(l, z, y):
    for x in range(4):
        turtle.forward(l)
        turtle.left(300)
        turtle.forward(l)
        turtle.left(120)
        turtle.forward(l)
        turtle.left(300)
        turtle.forward(l)
        if x % 2 == 0:
            turtle.left(300)
        else:
            turtle.left(120)
    if (z == 3) & (y % 2 == 0):
        turtle.left(180)
    if z == 4:
        if y % 2 == 0 or y % 3 == 0 or y == 11 or y == 19 or y == 35 or y == 43:
            if y == 9 or y == 15 or y == 21 or y == 33 or y == 39 or y == 45:
                turtle.left(0)
            else:
                turtle.left(180)

def run():
    l = 100  #Größe des Fraktals


    turtle.up()
    turtle.left(180)
    turtle.forward((l+l+(math.sqrt(pow(l/2,2)+pow(l,2))))/2)
    turtle.left(90)
    a = l * (-math.sin(60))
    turtle.forward(((math.sqrt(pow(l/2,2) + pow(l,2))*2)+(2 * a * (-math.sin(30))))/4)
    turtle.left(90)
    turtle.down()


    for x in range(48):    #Iterationstiefe > 1; 4
        a2(l/27, 4, x)
    for x in range(12):    #Iterationstiefe > 1; 3
        a2(l/9, 3, x)
    for x in range(3):    #Iterationstiefe > 1; 2
        a2(l/3, 2, 0)
    for x in range(3):    #Iterationstiefe 1
        a1(l)

run()

turtle.getscreen()._root.mainloop()
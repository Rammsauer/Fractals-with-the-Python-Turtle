import turtle

turtle.color('black')
s = [1,1,1,1,1,2,1,1,1,1,3]
i = 5
f1 = 3
f2 = 5
f3 = 8
v = 1                   
for x in s:
    turtle.fd(x*v)
    turtle.lt(90)
for x in range(0,4):
    turtle.fd(2*v)
    turtle.lt(90)
while x < i:
    turtle.fd(f2*v)
    turtle.lt(90)
    for x in range(0,4):
        turtle.fd(f1*v)
        turtle.lt(90)
    turtle.fd(f3*v)
    turtle.lt(90)
    for x in range(0,4):
        turtle.fd(f2*v)
        turtle.lt(90)
    f2=f2+f3        
    f1=f3           
    f3=f2+f3
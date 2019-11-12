from quanfunctions import *

turtle.bgcolor("red")
turtle.colormode(255)
turtle.tracer(False)
bob.shape("square")
for time in range(800):
    bob.pu()
    bob.forward(time)
    bob.left(200)
    bob.pd()
    bob.stamp()
    bob.left(15)
    tile("orange")

turtle.tracer(True)




        

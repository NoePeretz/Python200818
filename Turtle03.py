import turtle
import time

a = turtle.Turtle()
b = turtle.Turtle()

a.color('lightBlue')
b.color('violet')

a.pensize(5)
b.pensize(5)

for i in range(361):
    a.forward(1)
    a.right(1)
    
for i in range(361):
    b.forward(1)
    b.left(1)
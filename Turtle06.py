import turtle

n = int(input("How many lines would you like in your shape?:"))
for i in range(n):
    turtle.forward(100)
    turtle.left(360/n)
import turtle

turtle.shape("turtle")

n = int(input("輸入邊:"))

for i in range(n):
    turtle.forward(50)
    turtle.right(360/n)
    
turtle.done()
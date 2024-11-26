import turtle

screen = turtle.Screen()
pen = turtle
pen.pendown
for x in range(50):
    pen.left(30)
    pen.forward(20 + x)
pen.circle(5)


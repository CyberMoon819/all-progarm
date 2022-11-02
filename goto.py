import turtle
turtle.bgcolor("blue")
turtle.pensize(2)
turtle.speed(1)

for i in range(6):
    for colours in ["red","magenta","black","cyan","green"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
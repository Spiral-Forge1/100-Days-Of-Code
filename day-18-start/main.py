import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
# tim.shape("turtle")
# tim.color("black", "cyan")

# CHALLENGE 1
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# CHALLENGE 2
# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# CHALLENGE 3
# for i in range(3, 10):
#     r = random.randint(1, 255)
#     g = random.randint(1, 255)
#     b = random.randint(1, 255)
#     for _ in range(0, i):
#         turtle.colormode(255)
#         tim.pencolor(r, g, b)
#         tim.forward(100)
#         angle = round(360 / i)
#         print(angle)
#         tim.right(angle)

# CHALLENGE 4
# direction = [0,90,180,270]
# tim.pensize(15)
# tim.speed("fastest")
# turtle.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colors = (r, g, b)
#     return colors
#
# def turn(d):
#      for _ in range(200):
#         tim.color(random_color())
#         dd = random.choice(d)
#         tim.setheading(dd)
#         tim.forward(30)
#
# turn(direction)

# CHALLENGE 5
r = 75
tim.speed("fastest")
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors
def draw(size_gap):
    for i in range(int(360 / size_gap)):
        tim.color(random_color())
        tim.circle(r)
        tim.left(size_gap)
draw(5)




















screen = Screen()
screen.exitonclick()
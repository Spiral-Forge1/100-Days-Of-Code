# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)
import turtle

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136),
 (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
 (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
 (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
 (176, 192, 208), (168, 99, 102)]
import random
from turtle import Turtle, Screen
tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.hideturtle()
row = 11
def draw():
    space = 50
    for i in range(1, row):
        for j in range(1, 11):
            random_colors = random.choice(color_list)
            tim.dot(20, random_colors)
            tim.forward(50)
        tim.goto(0,space)
        space += 50
draw()






















screen = Screen()
screen.exitonclick()
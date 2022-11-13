from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []
is_race_on = False

pos_y = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x= -230, y=pos_y)
    pos_y += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"{winning_color} tutrle won, You won")
            else:
                print(f"{winning_color} turtle won, You lost")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
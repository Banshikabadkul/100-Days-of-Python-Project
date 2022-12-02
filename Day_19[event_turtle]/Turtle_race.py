from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="make a bet", prompt = "which title will win the race? Enter a color: ")
print(user_bet)
y_pos= [-70,-40,-10,20,50,80]
all_turtles = []

colors = ["red","yellow","green","orange","purple","blue"]
for tutle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[tutle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[tutle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won ! The {winning_color} turtle is winner")
            else:
                print(f"You've lost ! The {winning_color} turtle is winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)







screen.exitonclick()
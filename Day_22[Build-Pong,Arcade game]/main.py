from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create paddle

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with ball
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

# detect collision with right paddle
    if ball.distance(r_paddle) < 50 or ball.xcor() > 380 :
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 or ball.xcor() < -380 :
        ball.bounce_x()

    # detect r_paddle mises

    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()


screen.exitonclick()
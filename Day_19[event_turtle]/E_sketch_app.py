from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

tim.color("red")

screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="A", fun=counter_clockwise)
screen.onkey(key="D", fun=clockwise)
screen.onkey(key="C", fun=clear_drawing)

screen.exitonclick()
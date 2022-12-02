from turtle import Turtle


class Scoreboard(Turtle):
    def __int__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score()
        self.r_score()
        self
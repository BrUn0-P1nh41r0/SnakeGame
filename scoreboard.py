from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-10, 270)
        self.score(0)

    def score(self,score):
        self.clear()
        self.write(arg=f"Score: {score}", move=False, align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
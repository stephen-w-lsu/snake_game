from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 25, "bold")

class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setposition(x=0, y=0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
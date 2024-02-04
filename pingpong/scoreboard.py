from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.s1=0
        self.s2=0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.s1,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.s2,align="center",font=("Courier",80,"normal"))
    def l_point(self):
        self.s1+=1
        self.update_scoreboard()
    def r_point(self):
        self.s2+=1
        self.update_scoreboard()
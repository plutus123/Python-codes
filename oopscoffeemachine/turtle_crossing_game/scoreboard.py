from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.sco=0
        self.hideturtle()
        self.penup()
        
        self.level=1
        self.scoring()
    def score(self):
        self.clear()
        self.goto(0,280)
        self.write(f"Score : {self.sco}",align="center",font=("Courier", 15, "normal"))
        self.goto(0,0)
        self.write("GameOver",align="center",font=("Courier", 30, "normal"))
    def scoring(self):
        self.clear()
        self.goto(0,280)
        self.write(f"Score : {self.sco}",align="center",font=("Courier", 15, "normal"))
        self.goto(0,0)
        self.write(f"Level : {self.level}",align="center",font=("Courier", 15, "normal"))
    def score_up(self):
        
        self.sco+=1
        self.level+=1
        self.scoring()
        
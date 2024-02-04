from turtle import Turtle
class bar(Turtle):
    def __init__(self):
        super().__init__()
    def bar_length(self,position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position,0)
    def move_up(self):
        new_ycor=self.ycor() + 45
        self.goto(self.xcor(),new_ycor)
    def move_down(self):
        new_ycor=self.ycor() - 45
        self.goto(self.xcor(),new_ycor)
    
        
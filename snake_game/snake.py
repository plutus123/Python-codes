from turtle import Turtle
COORDINATES_LIST=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake():
    def __init__(self):
        self.segment=[]
        self.create_snake()
    def create_snake(self):
        for _ in COORDINATES_LIST:
           self.add(_)
    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            x=self.segment[seg_num-1].xcor()
            y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(x,y)
        self.segment[0].fd(MOVE_DISTANCE)
    def add(self,_):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(_)
        self.segment.append(new_segment)
    def extend_tail(self):
        self.add(self.segment[-1].position())
    def up(self):
        if self.segment[0].heading()!=DOWN:
            self.segment[0].setheading(UP)
    def right(self):
        if self.segment[0].heading()!=LEFT:
            self.segment[0].setheading(RIGHT)
    def left(self):
        if self.segment[0].heading()!=RIGHT:
            self.segment[0].setheading(LEFT)
    def down(self):
        if self.segment[0].heading()!=UP:
            self.segment[0].setheading(DOWN)
    def play_again(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake() 
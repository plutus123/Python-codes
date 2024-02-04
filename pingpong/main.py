from turtle import Turtle,Screen
from structure import bar
from ball_struct import ball
from scoreboard import Scoreboard
s=Scoreboard()
import time
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PingPong Game")
screen.tracer(0)
b=ball()
b1=bar()
b2=bar()
b1.bar_length(350)
screen.listen()
screen.onkey(b1.move_up,"Up")
screen.onkey(b1.move_down,"Down")
b2.bar_length(-350)
screen.listen()
screen.onkey(b2.move_up,"w")
screen.onkey(b2.move_down,"s")
is_true=True
while is_true:
    screen.update()
    time.sleep(b.move_speed)
    b.move()
    if b.ycor()>280 or b.ycor()<-280:
        b.bounce_y()
    if b.distance(b1)<55 and b.xcor()>320 or b.distance(b2)<55 and b.xcor()<-320:
        b.bounce_x()
    if b.xcor() > 380  :
        b.reset_pos()
        s.l_point()
    if b.xcor() < -380  :
        b.reset_pos()
        s.r_point()
screen.exitonclick()











screen.exitonclick()
from snake import Snake 
from turtle import Turtle,Screen
from food import Food
import time
from scoreboard import Score
v=Turtle()
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
s=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(s.up,"Up")
screen.onkey(s.right,"Right")
screen.onkey(s.left,"Left")
screen.onkey(s.down,"Down")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()
    if s.segment[0].distance(food)<15:
        food.refresh()
        score.increase_score()
        s.extend_tail()
    if s.segment[0].xcor()>280 or s.segment[0].xcor()<-280 or s.segment[0].ycor()<-280 or s.segment[0].ycor()>280:
       score.reset()
       s.play_again()
    for seg in s.segment[1:]:
        # if s.segment[0]==seg:
        #     pass
        if s.segment[0].distance(seg)<10:
            # score.is_game_over()    
            score.reset()
            s.play_again()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
screen.exitonclick()

import random
import turtle as t
s=t.Screen()
s.setup(650,650)
x=300
all_turtles=[]
user_bet=s.textinput("Make a bet","Which turtle will win the race?Enter the color")
colors=['red','orange','yellow','green','purple','blue']
for _ in range(0,6):
    v=t.Turtle(shape="turtle")
    v.color(colors[_])
    v.penup()
    v.goto(-300,x)
    x-=100
    all_turtles.append(v)
is_race_on=False
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>290:
            winning_color=turtle.pencolor()
            if user_bet==winning_color:
                print(f"The winnig color is {winning_color}.You have won")
            else:
                print(f"The winnig color is {winning_color}.You have lost")
            is_race_on=False
        distance=random.randint(0,10)
        turtle.forward(distance)
s.exitonclick()
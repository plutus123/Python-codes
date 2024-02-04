from turtle import Turtle,Screen
import pandas as pd
screen=Screen()

screen.listen()
screen.title("US states game")
screen.addshape("/Users/HP/Desktop/python/us state game/blank_states_img.gif")
turtle=Turtle()
turtle.shape("/Users/HP/Desktop/python/us state game/blank_states_img.gif")
def click(x,y):
    print(x,y)
answer_state=screen.textinput(title="Guess the State",prompt="What's another state's name?").lower()
# print(answer_state)
coordinates=screen.onscreenclick(click)
data=pd.read_csv("/Users/HP/Desktop/python/us state game/50_states.csv")
states=data["state"]
states=states.to_list()
x_cor=data["x"].to_list()
y_cor=data["y"].to_list()
is_true=True
guess=[]
count=0
while is_true:
    if answer_state=="exit":
        break
    for _ in range(0,50):
        if states[_].lower()==answer_state:
            t=Turtle()
            t.penup()
            t.hideturtle()
            t.goto(x_cor[_],y_cor[_])
            t.write(states[_],align="center",font=('Arial', 8, 'normal'))
            count+=1
            guess.append(states[_])
        else:
            continue
            break
        if count==50:
            is_true=False
    turtle.goto(0,0)
    answer_state=screen.textinput(title=f"{count}/50",prompt="What's another state's name?").lower()
new_list=list(set(states).difference(guess))
data_frame=pd.DataFrame(new_list)
data_frame.to_csv("anurag_the_great")
screen.mainloop()
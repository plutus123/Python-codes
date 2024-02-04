import turtle as t
v=t.Turtle()
screen=t.Screen()
def move_forward():
        v.fd(10)
def move_backward():
        v.back(10)
def move_clockwise():
        v.right(1)
def move_anticlockwise():
        v.left(1)
def clear():
        v.reset()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_clockwise,"d")
screen.onkey(move_anticlockwise,"a")
screen.onkey(clear,"c")
screen.listen()
screen.exitonclick()
import turtle as t
import random
tim=t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.speed("fastest")
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    my_tuple=(r,g,b)
    return my_tuple
def fun(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
fun(5)
my_screen=t.Screen()
my_screen.exitonclick()
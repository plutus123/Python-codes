import random
import turtle as t
timmy=t.Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.speed(0)
# for _ in range(0,10):
#     timmy.fd(10)
#     timmy.penup()
#     timmy.fd(10)
#     timmy.pendown()
# def fun(number_of_sides):
#     angle=360/number_of_sides
#     for _ in range(0,number_of_sides):
#         timmy.forward(100)
#         timmy.right(angle)
# for shape in range(3,10):
#     fun(shape)
# for _ in range(3):
#     timmy.color("coral")
#     timmy.forward(100)
#     timmy.right(120)
# for _ in range(4):
#     timmy.color("yellow")
#     timmy.forward(100)
#     timmy.right(90)
# for _ in range(5):
#     timmy.color("blue")
#     timmy.forward(100)
#     timmy.right(72)
# for _ in range(6):
#     timmy.color("black")
#     timmy.forward(100)
#     timmy.right(60)
# color=['blue','green','red','orange','violet','grey','black','brown','yellow','coral','purple','cyan']
t.colormode(255)
direction=[0,90,180,270]
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    my_tuple=(r,g,b)
    return my_tuple
for _ in range(0,200):
    timmy.color(random_color())
    timmy.pensize(10)
    timmy.seth(random.choice(direction))
    timmy.forward(50)
my_screen=t.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

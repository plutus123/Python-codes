# import colorgram
import random
import turtle as t
v=t.Turtle()
# colors=colorgram.extract('image.jpeg',30)
# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
t.colormode(255)
color_list=[(202,164,109),(238,240,245),(150,75,49),(223,201,135),(52,93,124),(172,154,40),(140,13,90),(23,240,24),(238,24,24),(238,24,24),(23,24,245),(23,240,24),(23,20,24)]
# print(color_list)
v.penup()
def fun(x,y):
    for f in range(0,15):
        v.setposition(-x,-y)
        y-=30
        for _ in range(0,10):
            v.dot(20,random.choice(color_list))
            v.forward(40)
fun(200,200)
screen=t.Screen()
screen.exitonclick()
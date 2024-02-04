from turtle import Turtle,Screen
timmy=Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.fd(100)
my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon Name",['Aditya','Anurag','Rohit'])
table.add_column("Type",['Fire','Water','Electric'])
table.align='l'
print(table)
# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("Pokemon Name",['Aditya','Anurag','Rohit'])
# table.add_column("Type",['Fire','Water','Electric'])
# table.align='l'
# print(table)
# class User:
#     pass
# user_1=User()
# user_1.id="Vishaws Mishra"
# print(user_1.id)
class Car:
    def __init__(self,seats,color):
        self.seats=seats
        self.color=color
car_1=Car(5,"Blue")
print(car_1.seats)
print(car_1.color)
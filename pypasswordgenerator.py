import random
import string
print("Welcome to PyPassword Generator! ")
c=int(input("How many letters you want in your password "))
password=""
random_password=[]
for x in range(0,c):
    x=random.choice(string.ascii_letters)
    password=password+x
    random_password+=x
d=int(input("How many symbols would you like? "))
for y in range(0,d):
    y=random.choice(string.punctuation)
    password=password+y
    random_password+=y
e=int(input("How many numbers would you like? "))
for z in range(0,e):
    z=str(random.randint(0,9))
    password=password+z
    random_password+=z
print(f"The Password is : {password}")
random.shuffle(random_password)
new_password = ""
for char in random_password:
    new_password+=char
print(new_password)
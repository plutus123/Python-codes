import os
from time import sleep
print("Welcome to secret auction program.")
money=0
word=""
is_true=True
while is_true:
    name=input("What is your name?: ")
    bid=int(input("Enter your bid: $"))
    bidders=input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if bidders=="yes":
        sleep(1)
        os.system('cls')
        if money<=bid:
            word=name
            money=bid
    elif bidders=="no":            
        print(f"The winner is {word} with bid of ${money}")
        is_true=False
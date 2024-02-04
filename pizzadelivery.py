print("Welcome to Python Pizza Deliveries")
size=input("What size of pizza do you want? S,M or L ")
add_pepironi=input("Do you want peporoni? Y or N ")
extra_cheese=input("Do you want extra cheese? Y or N ")
bill=0
if size=='S':
    bill=15
    print("The bill of pizza is $15")
elif size=='M':
    bill=20
    print("The bill of pizza is $20")
else:
    bill=25
    print("The bill of pizza is $25")
if add_pepironi=='Y':
    if size=='S':
        bill+=2
    else:
        bill+=3
if extra_cheese=='Y':
    bill+=1
print(f"The total bill is equal to ${bill}")
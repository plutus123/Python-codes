indigrents=[
    {
    'Water':300,
    'Milk':200,
    'Coffee':100,
    },
    {
    'Water':50,
    'Milk':0,
    'Coffee':18,
    },
    {
    'Water':250,
    'Milk':100,
    'Coffee':24,
    },
    {
    'Water':200,
    'Milk':150,
    'Coffee':24,
    }
]
cost=0
costs=0
list=[]
gist=[]
is_true=True
for _ in indigrents[0]:
    list.append(indigrents[0][_])        
while is_true:
    coffee=input("What would you like? Espresso, Latte, Cappuccino? ").lower()
    if coffee=='report':
        print(f"Water: {list[0]}ml")
        print(f"Milk: {list[1]}ml")
        print(f"Coffee: {list[2]}g")
        print(f"Money: ${cost}")
        continue
    elif coffee=='turnoff':
        is_true=False
    elif coffee=='espresso'and list[0]>=50 and list[1]>=0 and list[2]>=18:
        costs=1.50
        for _ in indigrents[1]:
            gist.append(indigrents[1][_])
        print("Please insert coins")
        quarter=int(input("How many quarter? "))
        dime=int(input("How many dime? "))
        nickel=int(input("How many nickel? "))
        penny=int(input("How many penny? "))
        total_money_inserted=(0.25*quarter)+(0.1*dime)+(0.05*nickel)+(penny*0.01)
        total_money=round(total_money_inserted,2)
        change=total_money-costs
        if change>0:
            print(f"Here is ${change} in change")
            print(f"Here is your {coffee}, Enjoy!")
        else:
            print("Sorry that's not enough money.Money refunded")
        if total_money<=1.5:
            continue
        
    elif coffee=='cappuccino' and list[0]>=250 and list[1]>=100 and list[2]>=24:
        costs=3.00
        for _ in indigrents[2]:
            gist.append(indigrents[2][_])
        print("Please insert coins")
        quarter=int(input("How many quarter? "))
        dime=int(input("How many dime? "))
        nickel=int(input("How many nickel? "))
        penny=int(input("How many penny? "))
        total_money_inserted=(0.25*quarter)+(0.1*dime)+(0.05*nickel)+(penny*0.01)
        total_money=round(total_money_inserted,2)
        change=total_money-costs
        if change>0:
            print(f"Here is ${change} in change")
            print(f"Here is your {coffee}, Enjoy!")
        else:
            print("Sorry that's not enough money.Money refunded")
        if total_money<=3.00:
            continue
        
    elif coffee=='latte' and list[0]>=200 and list[1]>=150 and list[2]>=24:
        costs=2.50
        for _ in indigrents[3]:
            gist.append(indigrents[3][_])
        print("Please insert coins")
        quarter=int(input("How many quarter? "))
        dime=int(input("How many dime? "))
        nickel=int(input("How many nickel? "))
        penny=int(input("How many penny? "))
        total_money_inserted=(0.25*quarter)+(0.1*dime)+(0.05*nickel)+(penny*0.01)
        total_money=round(total_money_inserted,2)
        change=total_money-costs
        if change>0:
            print(f"Here is ${change} in change")
            print(f"Here is your {coffee}, Enjoy!")
        else:
            print("Sorry that's not enough money.Money refunded")
        if total_money<=2.50:
            continue
        
    if coffee=='espresso':
        if list[0]<50:
            print("Sorry there is not enough water")
            continue
        if list[1]<0:
            print("Sorry there is not enough milk")
            continue
    if coffee=='cappuccino':
        if list[0]<250:
            print("Sorry there is not enough water")
            continue
        if list[1]<100:
            print("Sorry there is not enough milk")
            continue
        if list[2]<18:
            print("Sorry there is not enough coffee")
            continue
    if coffee=='latte':
        if list[0]<200:
            print("Sorry there is not enough water")
            continue
        if list[1]<150:
            print("Sorry there is not enough milk")
            continue
        if list[2]<18:
            print("Sorry there is not enough coffee")
            continue
    if (coffee=='espresso'and list[0]>=50 and list[1]>=0 and list[1]>=18) or (coffee=='cappuccino' and list[0]>=250 and list[1]>=100 and list[2]>=24) or (coffee=='latte' and list[0]>=200 and list[1]>=150 and list[2]>=24):
        list[0]=list[0]-gist[0]
        list[1]=list[1]-gist[1]
        list[2]=list[2]-gist[2]
        gist=[]
    cost=cost+costs
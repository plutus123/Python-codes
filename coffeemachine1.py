MENU={
    "espresso":{
    "indegrients":{
    "water":50,
    "coffee":18
    },
   " cost":1.50
    },
    "latte":{
    "indegrients":{
    "water":200,
    "milk":150,
    "coffee":24
    },
   " cost":2.50
    },
    "cappucino":{
    "indegrients":{
    "water":250,
    "milk":100,
    "coffee":24
    },
   " cost":3.00
    },
}
resources={
    "water":300,
    "milk":200,
    "coffee":100
}
is_on=True
profit=0
def is_resource_sufficient(order_indegrients):
    for item in order_indegrients:
        if order_indegrients[item]>resources[item]:
            print(f"Sorry not enough {item}")
            return False
    return True
def process_coins():
    print("Please insert coins")
    total=int(input("how many quarters"))*0.25
    total+=int(input("how many dimes"))*0.10
    total+=int(input("how many nickels"))*0.05
    total+=int(input("how many pennies"))*0.01
    return total
def is_transaction_successful(money_received,drink_cost):
    if money_received>drink_cost:
        change=round(money_received - drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else :
        print("Sorry that's not enough money.Money refunded")
        return False
def make_coffee(drink_name,order_indegrients):
    for item in order_indegrients:
        resources[item]-=order_indegrients[item]
    print(f"Here is your {drink_name}")
while is_on:
    choice=input("What would you like? espresso/latte/cappucino: ").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["indegrients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["indegrients"])
import random
is_true=True
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
while is_true:
    blackjack=input("Do you want to play blackjack game? Type 'y' or 'n': ").lower()
    if blackjack=='y':
        a=random.choice(cards)
        b=random.choice(cards)
        c=a+b
        another_card=random.choice(cards)
        d=c+another_card
        print(f"Your cards are: [{a},{b}]")
        x=random.choice(cards)
        y=random.choice(cards)
        z=x+y
        r=random.choice(cards)
        t=z+r
        print(f"Computer's first card: {x}")
        risk=input("Type 'y' to get another card, 'n' to pass: ").lower()
        if risk=='n':
            if z>17:
                print(f"Your final hand: [{a},{b}]")
                print(f"Computer's final hand: [{x},{y},{r}]")
                if c>t:
                    print("You win")
                elif c<t:
                    print("You lose")
                elif c==t:
                    print("Draw")
            else:
                print(f"Your final hand: [{a},{b}]")
                print(f"Computer's final hand: [{x},{y}]")    
                if c>z:
                    print("You win")
                elif c<z:
                    print("You lose")
                elif c==z:
                    print("Draw")
        elif risk=='y':
            if z<=17:
                print(f"Your final hand: [{a},{b},{another_card}]")
                print(f"Computer's final hand: [{x},{y}]")
                if d>z and d<=21:
                    print("You win")
                elif d<z:
                    print("You lose")
                elif d>21:
                    print("You lose")
                elif d==z:
                    print("Draw")
            elif z>17:
                print(f"Your final hand: [{a},{b},{another_card}]")
                print(f"Computer's final hand: [{x},{y},{r}]")
                if d>t and d<=21:
                    print("You win")
                elif d<t and t<=21:
                    print("You lose")
                elif d>21:
                    print("You lose")
                elif d==t:
                    print("Draw")
                elif t>21 and d<=21:
                    print("You win")
                elif t>21 and d>21:
                    print("Draw")
    else:
        is_true=False
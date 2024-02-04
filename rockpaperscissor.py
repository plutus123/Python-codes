import random
c = int(input("What do you choose? 0 for rock , 1 for paper and 2 for scissors "))
if c == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif c == 1:
    # Paper
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    # Scissors
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print("Computer choose:")
d=random.randint(0,2)
if d == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif d == 1:
    # Paper
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    # Scissors
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if c==0 and d==0:
    print("Draw")
elif c==1 and d==1:
    print("Draw")
elif c==2 and d==2:
    print("Draw")
elif c==0 and d==1:
    print("You lose")
elif c==0 and d==2:
    print("You Win")
elif c==1 and d==0:
    print("You Win")
elif c==1 and d==2:
    print("You lose")
elif c==2 and d==0:
    print("You lose")
elif c==2 and d==1:
    print("You Win")
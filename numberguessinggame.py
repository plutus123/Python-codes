import random
print("Welcome to number guessing game!")
print("I'm thinking of a number between 1 and 100")
difficulty=input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
number=random.randint(1,100)
attempts=0
if difficulty=='easy':
    attempts=10
elif difficulty=='hard':
    attempts=5
is_game=True
def fun(attempts):
    print(f"You have {attempts} attempts remaining to guess the number")
    guess=int(input("Make a guess: "))
    if guess==number:
        print(f"You got it, The answer was {guess}")
    elif guess>number:
        print("Too high")
        print("Guess again")
    elif guess<number:
        print("Too low")
        print("Guess again")
while is_game:
    if difficulty=='hard':
        fun(attempts)
        attempts-=1
    elif difficulty=='easy':
        fun(attempts)
        attempts-=1  
    if attempts==0:
        print("You lose")
        is_game=False
import random
import higherlowergamedata
import os
import logohigherlower
is_game_over=False
current_score=0
A=random.choice(higherlowergamedata.data)
B=random.choice(higherlowergamedata.data)
while A==B:
    A=random.choice(higherlowergamedata.data)
while not is_game_over:
    list_A=[]
    list_B=[]
    for word in A:
        list_A.append(A[word])
    followers_of_A=list_A.pop(1)
    print(logohigherlower.logo[0])
    print(f"Compare A: {' , '.join(list_A)}")
    for word in B:
        list_B.append(B[word])
    followers_of_B=list_B.pop(1)
    print(logohigherlower.logo[1])
    print(f"Against B: {' , '.join(list_B)}")
    Your_choice=input("Who has more follower? A or B: ").upper()
    if Your_choice=='A':
        if followers_of_A>followers_of_B:  
            current_score+=1
            os.system('cls')
            print(f"You are right! Current score: {current_score}")
            A=B
            B=random.choice(higherlowergamedata.data)
        elif followers_of_A<followers_of_B:
            print("You lose")
            os.system('cls')
            is_game_over=True
    elif Your_choice=='B':
        if followers_of_B>followers_of_A:  
            current_score+=1
            os.system('cls')
            print(f"You are right! Current score: {current_score}")
            A=B
            B=random.choice(higherlowergamedata.data)
        elif followers_of_B<followers_of_A:
            print("You lose")
            os.system('cls')
            is_game_over=True
print(logohigherlower.logo[0])
print(f"Sorry that's wrong, Your final score is: {current_score}")
import random
import os
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def play_game():
    is_game_over=False
    players_card=[]
    computers_card=[]
    for _ in range(0,2):
        players_card.append(deal_card())
        computers_card.append(deal_card())
    def compare(computer_score,user_score):
        if user_score==computer_score:
            return "Draw"
        elif computer_score==0:
            return "Lose, an opponent has blackjack"
        elif user_score==0:
            return "Win with a blackjack"
        elif user_score>21:
            return "You went over,you lose"
        elif computer_score>21:
            return "Opponent went over,you win"
        elif user_score>computer_score:
            return "You win"
        else:
            return "You lose"
    def calculate_score(cards):
        if sum(cards)==21 and len(cards)==2:
            return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    user_score=calculate_score(players_card)
    computer_score=calculate_score(computers_card)
    while not is_game_over:
        user_score=calculate_score(players_card)
        computer_score=calculate_score(computers_card)
        print(f"Your cards : {players_card}, and current score: {user_score}")
        print(f"Computer's first card : {computers_card[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to draw another card or 'n' to pass: ")
            if user_should_deal=='y':
                players_card.append(deal_card())
            else :
                is_game_over=True
    while computer_score!=0 and computer_score<17:
        computers_card.append(deal_card())
        computer_score=calculate_score(computers_card)
    print(f"Your final hand is {players_card} and final score is {user_score}")
    print(f"Computer's final hand is {computers_card} and final score is {computer_score}")
    print(compare(computer_score,user_score))
while input("Do you want to play the game of Blackjack, Typer 'y' or 'n': ")=='y':
    os.system('cls')
    play_game()
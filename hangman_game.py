import random
import hangmanword
import os
from time import sleep
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')
#word_list=['ardvark','baboon','camel']
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
      ''']
chosen_word=random.choice(hangmanword.word_list)
print(f"The chosen word is {chosen_word}")
display=[]
for n in range(0,len(chosen_word)):
    display+="_"
end_of_game=False
lives=0
while not end_of_game:
    guess=input("Guess the word: ").lower()
    if guess in display:
      print("You have already guessed this")
    for position in range(0,len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=guess
    if guess not in chosen_word:
        print("You guessed a letter that is not in the chosen word and hence you lose a life. ")
        print(HANGMAN[lives])
        lives+=1
    print(' '.join(display))
    sleep(5)
    os.system('cls')
    if lives==7:
            end_of_game=True
            print("You lose")
    if "_" not in display:
        end_of_game=True
        print("You win")
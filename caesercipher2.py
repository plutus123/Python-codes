alphabet="a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
def fun():
    direction=input("Type 'encode' to encrypt, 'decode' to decrypt:\n")
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    def caeser(plain_text,shift_amount,direction):
        letter=""
        for word in plain_text:
            if word in alphabet:
                position=alphabet.index(word)
                if direction=="decode":
                    shift_amount*=-1
                new_position=position+shift_amount
                new_position=new_position % 26
                new_word=alphabet[new_position]
                letter+=new_word
            else:
                letter+=word
        print(f"The {direction}d word is: {letter}")
    caeser(plain_text=text,shift_amount=shift,direction=direction)
fun()
end_of_game=True
while end_of_game:
    k=input("Type Yes to continue or No to exit ").lower()
    if k=="yes":
        fun()
    else:
        print("Good Bye")
        end_of_game=False
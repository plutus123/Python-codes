alphabet="a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
direction=input("Type 'encode' to encrypt, 'decode' to decrypt:\n")
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))
def encrpt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")
def decrpt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"The decoded text is {cipher_text}")
if direction=="encode":
    encrpt(plain_text=text,shift_amount=shift)
elif direction=="decode":
    decrpt(plain_text=text,shift_amount=shift)
import pandas as pd
user_input=input("Enter your name: ").upper()
data=pd.read_csv("/Users/HP/Desktop/python/nato/nato_phonetic_alphabet.csv")
# print(data.to_dict())
is_true=True
while is_true:
    try:
        dict={row.letter:row.code for (index,row) in data.iterrows()}
        list=[dict[item] for item in user_input]
        print(list)
        is_true=False
    except KeyError:
        user_input=input("Enter your name: ").upper()
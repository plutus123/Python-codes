import os
print("Welcome to blind auction: ")
is_true=True
bids={}
def fun(bidding_record):
    money=0
    winner=""
    for n in bidding_record:
        bid_amount=bidding_record[n]
        if bid_amount>money:
            money=bid_amount
            winner=n
    print(f"The winner of the auction is {winner} with a bid of ${money}")
while is_true:        
    name=input("What is your name?: ")
    bid=int(input("Enter your bid: $"))
    bidders=input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    bids[name]=bid
    if bidders=="yes":
        os.system("cls")
    else:
        fun(bids)
        is_true=False

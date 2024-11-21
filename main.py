import os
#Hint: You can call clear() to clear the output in the console.

from art import logo
print(logo)
bids = {}
biding_finish = False

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Alireza": 100,"Hamid": 200}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bid}")

while not biding_finish:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        biding_finish = True
        find_highest_bidder(bids)
    elif should_continue =="yes":
        cls()

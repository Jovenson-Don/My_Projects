bid_on = True
auction = {}

def winner():
    highest_bid_winner = ""
    highest_bid = 0
    for bid in auction:
        if auction[bid] > highest_bid:
            highest_bid = auction[bid]
            highest_bid_winner = bid
    return f"The winner is {highest_bid_winner} with the highest bid of ${highest_bid}!"


while bid_on is True:
# TODO-1: Ask the user for input
    name = input("What is your name? ")
    bidding = int(input("What is your bid? "))
# TODO-2: Save data into dictionary {name: price}
    auction.update({name:bidding})
# TODO-3: Whether if new bids need to be added
    another_bidder = input("Is there another bidder? ")
    if another_bidder == "yes":
        print("\n" * 20)
# TODO-4: Compare bids in dictionary
    else:
        bid_on = False
        winner = winner()
        print(winner)



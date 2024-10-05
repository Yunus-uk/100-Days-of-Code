# TODO-1: Ask the user for input
import art
print(art.logo)

more_bidders = "yes"
auction = {}
while more_bidders == "yes":
    auction.update({input("What is your name?: "): int(input("What is your bid?: $"))})
    more_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n")
    print("\n" * 100)
else:
    maximum = 0
    for key in auction:
        if auction[key] > maximum:
            maximum = auction[key]
    for key in auction:
        if maximum == auction[key]:
            print(f"The winner is {key} with a bid of ${maximum}")






#def add_bidders(bidders, name = name, bid = bid):
#    new_bidders = {}
#    for key in bidders:
#        new_bidders[name] = bid
#    return new_bidders
#    add_bidders(name,bid)
#stop_bidding = False


#auction = {}
#def start_biding():
#    stop_bidding = False
#    while not stop_bidding:
#        auction.update({input("What is your name?: "):int(input("What is your bid?: $"))})
#        print(auction)
    #print("\n" * 100)
    #print(auction)

# TODO-2: Save data into dictionary {name: price}
#start_biding()
# TODO-3: Whether if new bids need to be added
#more_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n")
#if more_bidders == "yes":
#    start_biding()
#else:
#    stop_bidding = True
#while more_bidders == "yes":
    #more_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n")
    #print("\n" * 100)
 #   start_biding()

# TODO-4: Compare bids in dictionary
# The winner is h with a bid of $6
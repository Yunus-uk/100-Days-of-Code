import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #cards = [11, 10, 7]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21:
        return 0
    elif sum(cards) > 21:
        for card in cards:
            if card == 11:
                cards.remove(11)
                cards.append(1)
                print(cards)
                print(sum(cards))
    else:
        return sum(cards)

def final_hand():
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")


def outcome():
    if calculate_score(user_cards) == 0:
        final_hand()
        print("Win")
        exit()
    elif calculate_score(computer_cards) == 0:
        final_hand()
        print("Lose")
        exit()
    elif sum(user_cards) > 21:
        final_hand()
        print("Lose")
        exit()

def compare(user, computer):
    if user == computer:
        print("Draw")
    elif computer == 0:
        print("Lose")
    elif user == 0:
        print("Win")
    elif user > 21:
        print("Lose")
        print(computer)
    elif computer > 21:
        print("computer > 21")
        print("Win")
    elif user > computer:
        print("user > computer")
        print("Win")
    else:
        print("Lose")
        print(computer)


print(art.logo)
user_cards = []
computer_cards = []

user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards.append(deal_card())
computer_cards.append(deal_card())

print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
print(f"Computer's first card: {computer_cards[0]}")

outcome()

another_card = input("Type 'y' to get another card, type 'n' to pass: ")
while another_card == 'y':
    user_cards.append(deal_card())
    calculate_score(user_cards)
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    while sum(computer_cards) < 17:
        computer_cards.append(deal_card())
    outcome()
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
while another_card == 'n':
    if sum(computer_cards) < 17:
        computer_cards.append(deal_card())
    else:
        final_hand()
        compare(sum(user_cards), sum(computer_cards))
        exit()

final_hand()
compare(sum(user_cards),sum(computer_cards))






# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# card1 = random.choice(cards)
# card2 = random.choice(cards)
# computer_card1 = random.choice(cards)
# computer_card2 = random.choice(cards)
# user_score = add(card1,card2)
# computer_score = add(computer_card1,computer_card2)
# print(f"Card1: {card1}")
# print(f"card2: {card2}")
# print(user_score)
# print(computer_score)

# print(f"Your cards: {card1, card2}, current score: {user_score}")
# print(f"Computers first card: {computer_card1}")
# if user_score == 21:
#     print ("Win")
# elif computer_score == 21:
#     print ("Lose")
# elif user_score > 21:
#     if card1 == 11:
#         card1 = -10
#     elif card2 == 11:
#          card2 = -10
# cont = input("Type 'y' to get another card, type 'n' to pass: ")
# while cont =='Y':
#     blackjack()







# print(f"Your cards: {card1, card2}, current score: {user_score}")
# print(f"Computers first card: {computer_card1}")
#
# cont = input("Type 'y' to get another card, type 'n' to pass: ")
# if cont == 'y' and user_score <= 21:
#     card3 = random.choice(cards)
#     user_score += card3
#     print(f"Your cards: {card1, card2, card3}, current score: {user_score}")
#     print(f"Computers first card: {computer_score}")



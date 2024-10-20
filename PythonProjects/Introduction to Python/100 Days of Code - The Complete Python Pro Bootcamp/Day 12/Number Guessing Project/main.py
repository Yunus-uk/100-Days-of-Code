import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

while True:
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy" or level == "hard":
        break
    else:
        print("Wrong input, try again")

def check_number(guess):
    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print(f"You got it! The answer was {number}.")
        exit()

if level == 'easy':
    count = 10
    guess = ""
    while guess != number and count != 0:
        print(f"You have {count} attempts remaining to guess the number.")
        count -= 1
        guess = int(input("Make a guess: "))
        if count == 0:
            check_number(guess)
            print("You've run out of guesses, you lose.")
            exit()
        check_number(guess)
        print("Guess again")

if level == 'hard':
    count = 5
    guess = ""
    while guess != number and count != 0:
        print(f"You have {count} attempts remaining to guess the number.")
        count -= 1
        guess = int(input("Make a guess: "))
        if count == 0:
            check_number(guess)
            print("You've run out of guesses, you lose.")
            exit()
        check_number(guess)
        print("Guess again")

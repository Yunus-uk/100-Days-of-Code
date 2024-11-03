MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}

money = 0

# TODO 1. Print the report of all the coffee machine resources.
def report():
    ingredient_water = round(resources["water"],2)
    ingredient_milk = round(resources["milk"],2)
    ingredient_coffee = round(resources["coffee"],2)
    profit = round(resources["profit"],2)
    print(f"Water: {ingredient_water}\nMilk: {ingredient_milk}\nCoffee: {ingredient_coffee}\nProfit: ${profit}")

# TODO 3. Process Coins after sufficient resources.
def process_coins(quarters, dimes, nickels, pennies):
    global money
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01

    quarter *= quarters
    print(round(quarter,2))
    dime *= dimes
    print(round(dime,2))
    nickel *= nickels
    print(round(nickel,2))
    penny *= pennies
    print(round(penny,2))

    money = quarter + dime + nickel + penny

    return round(money,2)



# TODO 2. Check the resources sufficient to make drink order.
def check_drink(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        start()
    elif "milk" in MENU[drink]["ingredients"] and resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        # Only check milk if the drink requires it
        print("Sorry there is not enough milk.")
        start()
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough milk")
        start()
    else:
        print("Please insert coins:")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        process_coins(quarters, dimes, nickels, pennies)

# TODO 5. Make the coffee and reduce the resources.
def make_coffee(coffee):
    for ingredient, required_amount in MENU[coffee]["ingredients"].items():
        if ingredient in resources:
            # Calculate the new value by subtracting the required amount from the available amount
            resources[ingredient] -= required_amount
    print(f"Here is your {drink} ☕️. Enjoy!")


# TODO 4. Check Transaction successful, correct amount inserted.
def check_transaction(money):
    if drink == "latte":
        if money>= 2.5:
            money-=2.5
            resources["profit"] += 2.5
            print(f"Here is ${round(money,2)} dollars in change.")
            make_coffee('latte')
        else:
            print(f"Sorry that is not enough money. {round(money,2)} refunded")
    elif drink == "espresso":
        if money >= 1.5:
            money -= 1.5
            resources["profit"] += 1.5
            print(f"Here is ${round(money,2)} dollars in change.")
            make_coffee('espresso')
        else:
            print(f"Sorry that is not enough money. {round(money,2)} refunded")
    elif drink == "cappuccino":
        if money >= 3.0:
            money -= 3.0
            resources["profit"] += 3.0
            print(f"Here is ${round(money,2)} dollars in change.")
            make_coffee('cappuccino')
        else:
            print(f"Sorry that is not enough money. {round(money,2)} refunded")
            exit()

# TODO 6. Prompt User for type of drink wanted.
def start():
    while True:
        global drink
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
# TODO 7. Turn off coffee machine by entering 'off' at the prompt.
        if drink == "off":
            exit()
        elif drink == "report":
            report()
        else:
            check_drink(drink)
            check_transaction(money)
start()
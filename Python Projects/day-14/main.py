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
}


def start_coffeemaker():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = 0

    # TODO: 6. Calculate coins.
    def process_coin(coffee_choice, quarters, dimes, nickels, pennies):
        quarters_entered = .25 * quarters
        dimes_entered = .10 * dimes
        nickels_entered = .05 * nickels
        pennies_entered = .01 * pennies
        total_coins = quarters_entered + dimes_entered + nickels_entered + pennies_entered
        change = quarters_entered + dimes_entered + nickels_entered + pennies_entered - MENU[coffee_choice]['cost']
        if total_coins > MENU[coffee_choice]['cost']:
            print(f"Here is your change: ${round(change, 2)}")
            return change
        else:
            print("You do not have enough coins. Money refunded")

    def used_water(coffee_choice):
        return MENU[coffee_choice]['ingredients']['water']

    def used_milk(coffee_choice):
        if coffee_choice != 'espresso':
            return MENU[coffee_choice]['ingredients']['milk']
        else:
            return 0

    def used_coffee(coffee_choice):
        return MENU[coffee_choice]['ingredients']['coffee']

    drink = ''
    while drink != 'off':
        # TODO: 1. Prompt user for coffee.
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        # TODO: 5. Turn off coffeemaker with 'off'.
        if drink == 'off':
            drink = 'off'
        # TODO: 4. Check resources with 'report'.
        elif drink == 'report':
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"${round(money,2)}")
        else:
            # TODO: 2. Prompt user to enter coins. (quarters/dimes/nickels/pennies).
            print("Please insert coin.")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickel = int(input("How many nickels?: "))
            penny = int(input("How many pennies?: "))
            # TODO: 7. Adjust resources after every transaction
            if water < used_water(drink):
                print("Not enough water")
            elif milk < used_milk(drink):
                print("Not enough milk")
            elif coffee < used_coffee(drink):
                print("Not enough coffee")
            else:
                water -= used_water(drink)
                milk -= used_milk(drink)
                coffee -= used_coffee(drink)
                money += process_coin(drink, quarter, dime, nickel, penny)
                print(f"Here is your {drink}☕. Enjoy!")


start_coffeemaker()

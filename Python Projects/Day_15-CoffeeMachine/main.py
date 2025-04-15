# Menu dictionary containing drink types, their ingredients, and cost
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

# Initial available resources in the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Function to check if the user has inserted enough money
def check_money(num_quarters, num_dimes, num_nickels, num_pennies, drink):
    total_quarters = 0.25 * num_quarters
    total_dimes = 0.10 * num_dimes
    total_nickels = 0.05 * num_nickels
    total_pennies = 0.01 * num_pennies
    total = total_quarters + total_dimes + total_nickels + total_pennies

    cost = MENU[drink]["cost"]

    if total < cost:
        print(f"Not enough cash. Here is your refund ${total}")

    else:
        print(f"Here is your change ${round(total - cost, 2)}")
        make_drink(drink)
        update_register(cost)

# Function to simulate serving the drink
def make_drink(ordered_drink):
    print(f"Here is your {ordered_drink}. Enjoy!")

# Function to display current resource status
def format_resources():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

# Function to deduct used ingredients from the machine's resources
def update_resource(drink):
    if drink != "espresso":
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]

# Function to check if there are enough resources to make the drink
def check_resources(drink):
    if drink != "espresso":
        if MENU[drink]["ingredients"]["milk"] > resources["milk"]:
            print("Not enough milk.")
            return False

    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Not enough water.")
        return False

    elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Not enough coffee.")
        return False

    return True

# Function to update the machine's money after a purchase
def update_register(cash):
    global money
    money += cash


# Main program loop
money = 0
while_on = True

while while_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "report":
        # Display current resource levels and money
        format_resources()
    elif order == "off":
        # Shut down the machine
        while_on = False
    else:
        # Process drink order
        results = check_resources(order)
        if results:
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            check_money(quarters, dimes, nickels, pennies, order)
            update_resource(order)

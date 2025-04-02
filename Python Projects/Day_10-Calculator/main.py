from art import logo

# Create functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {"+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
            }
# Declare variables
print(logo)
is_on = True
first_number = float(input("Select first number: "))

# Ask for inputs and display results
while is_on is True:
    operator = input("'*'\n'+'\n'-'\n'/'\n Select an operator: ")
    second_number = float(input("Select a another number: "))
    results = operation[operator](first_number, second_number)
    first_number = results
    go_on = input(f"Type 'y' to continue with {results} or type 'n' to exit: ")
    if go_on == "n":
        print("Goodbye!")
        is_on = False
    else:
        continue



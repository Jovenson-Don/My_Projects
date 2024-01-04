from art import logo
# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    return n1 * n2


# Division
def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operation:
        print(symbol)
    keep_calculating = True

    while keep_calculating is True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        calculate_more = (input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit.: "))

        if calculate_more == "y":
            keep_calculating = True
            num1 = answer
        else:
            keep_calculating = False
            calculator()


calculator()

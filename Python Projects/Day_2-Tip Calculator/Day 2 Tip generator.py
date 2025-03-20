# Grab total amount of bill
bill = float(input("What is the final bill amount?\n"))

# Grab tip of total bill
tip_amount = int(input("How much tip do you want to give?\n"))
tip = (tip_amount / 100 * bill)

# Grab total number people
people = int(input("How many people to split against?\n"))

# Calculate total bill with tip
total_bill = bill + tip

# Calculate total amount per person with tip
amount_per_person = "{:.2f}".format(total_bill / people,)
print(f"Amount due per person.... ${amount_per_person}")

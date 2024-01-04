#Welcome user
print("Welcome to the tip calcuator!\n")
#Grab total bill amount with int
bill = float(input("What is the bill amount?\n"))
#Ask user how much tip they want
tip_percentage = int(input("How much would you like to tip?\n"))
#Ask user how much people to split bill
people = int(input("How many people do you want to split bill with?\n"))
#Calcuate tip
tip = bill * (tip_percentage / 100)
total_bill = tip + bill
#Amount due per person
bill_per_person = round(total_bill / people, 2)
#Output final number
print(f"Everyone owes {bill_per_person}")
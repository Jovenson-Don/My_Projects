file = open("../day-24/Input/Letters/starting_letter.txt")
letter = file.read()


data = open("../day-24/Input/Names/invited_names.txt")
names = data.readlines()

replace_name = "[name]"
for name in names:
    stripped_name = name.strip()
    new_letter = letter.replace(replace_name, stripped_name)
    with open(f"../day-24/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as finish_letter:
        finish_letter.write(letter)



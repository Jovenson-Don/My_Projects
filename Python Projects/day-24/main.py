# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


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



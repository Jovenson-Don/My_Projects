hangman = []
guessed_letter = []
chosen_word = input("Enter a word: ")

for _ in chosen_word:
    hangman.append("-")
print(hangman)

lives = 6
while lives > 0:
    letter = input("Enter a letter: ").lower()
    for position in range(len(chosen_word)):
        if letter == chosen_word[position]:
            hangman[position] = letter
            print(hangman)

    if letter not in chosen_word:
        lives -= 1
        print(f"{letter} is not in the word. Lives: {lives}")
    if letter not in guessed_letter and letter not in chosen_word:
        guessed_letter.append(letter)


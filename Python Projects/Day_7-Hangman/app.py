import random
import hangman_words
from hangman_art import stages

# Choose a random word for game and set word length
word_list = ["game", "friends", "loser"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Number of lives
lives = 6

# Show player chosen word with "-"
missing_letter = []
print(chosen_word)
for i in chosen_word:
    missing_letter.append("-")

print("".join(missing_letter))

while "-" in missing_letter:
    # Ask user to guess letter
    guess_letter = input("Guess a letter: ").lower()

    #Loop through word to add letter
    for i in range(word_length):
        if guess_letter == chosen_word[i]:
            missing_letter[i] = guess_letter
            print(stages[lives])
        else:
            lives -= 1
            print(stages[lives])
    print("".join(missing_letter))
print("Game over. You win!")


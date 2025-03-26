import random
import hangman_words
from hangman_art import logo, stages

# Initialize variables
words = hangman_words.word_list
chosen_word = random.choice(words)
word_length = len(chosen_word)
lives = 6
end_of_game = False
guessed_letters = []

# Display logo
print(logo)

# Create blanks
display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check if guess is in the word
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print(f"Good guess! {' '.join(display)}")
    else:
        print(f"'{guess}' is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The chosen word was '{chosen_word}'")
            break

    # Check if the player has guessed all the letters
    if "_" not in display:
        end_of_game = True
        print("Congratulations! You win!")

    # Show remaining lives and guessed letters
    print(stages[lives])
    print(f"Guessed letters: {', '.join(guessed_letters)}")

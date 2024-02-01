import random
import hangman_words
from hangman_art import logo, stages

words = hangman_words.word_list
chosen_word = random.choice(words)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)
# Create blanks
display = []
for _ in range(word_length):
    display += "_"
guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed this {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)

    if guess not in guessed_letters:
        guessed_letters += guess

    if guess not in chosen_word:
        print(f"{guess} is not in this word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.The chosen word was " + chosen_word)
        # Join all the elements in the list and turn it into a String.

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
    print(f"These are the letters you guessed so far {guessed_letters}")
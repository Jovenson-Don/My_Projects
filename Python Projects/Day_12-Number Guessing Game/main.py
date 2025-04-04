import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Define the game function
def play_game(game_mode):
    # Set number of lives based on difficulty
    if game_mode == 'easy':
        lives = 10
    else:
        lives = 5

    print(f"You have {lives} lives!")

    # Game loop: keep asking until lives run out or player guesses correctly
    while lives > 0:
        guess = int(input("Make a guess: "))

        # Check if the guess is correct
        if guess == random_number:
            print(f"You win! The number WAS {random_number}!")
            break
        else:
            lives -= 1  # Decrease lives by 1

            # Give feedback on the guess
            if guess > random_number:
                print(f"Your number is lower than the selected number! Try again...{lives} lives left.")
            elif guess < random_number:
                print(f"Your number is higher than the selected number! Try again...{lives} lives left.")

    # If out of lives, inform the player
    if lives == 0:
        print(f"You lose! The number was {random_number}.")

# Game introduction
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

# Ask for difficulty level
difficulty = input("Choose a difficulty. 'easy' or 'hard': ")

# Start the game
play_game(difficulty)

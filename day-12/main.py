from art import logo
import random

RANDOM_NUMBER = random.randint(1, 100)


# Easy function
def easy():
    lives = 10
    while lives > 0:
        guess = int(input(f"""You have {lives} attempts remaining to guess the number.
Make a guess: """))
        if guess < RANDOM_NUMBER:
            lives -= 1
            print("""Too low.
Guess again.""")
        elif guess > RANDOM_NUMBER:
            lives -= 1
            print("""Too High.
Guess again.""")
        else:
            print(f"You got it! The answer was {RANDOM_NUMBER}.")
            lives = 0
    if guess != RANDOM_NUMBER:
        print(f"You lose. {RANDOM_NUMBER} was the answer.")


# Hard function
def hard():
    lives = 5
    while lives > 0:
        guess = int(input(f"""You have {lives} attempts remaining to guess the number.
Make a guess: """))
        if guess < RANDOM_NUMBER:
            lives -= 1
            print("""Too low.
Guess again.""")
        elif guess > RANDOM_NUMBER:
            lives -= 1
            print("""Too High.
Guess again.""")
        else:
            print(f"You got it! The answer was {RANDOM_NUMBER}.")
            lives = 0
    if guess != RANDOM_NUMBER:
        print(f"You lose. {RANDOM_NUMBER} was the answer.")


# Print logo and explain game
def start_game():
    print(logo)
    print("""Welcome to the Number Guessing!
	I'm thinking of number between 1 and 100.""")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        easy()
    else:
        hard()

from art import logo, vs
from game_data import data
from random import randint

# Function to check if the player's answer is correct
def check_answer(response):
    global score
    correct = (player_1_followers > player_2_followers and response == 1) or \
              (player_2_followers > player_1_followers and response == 2)

    if correct:
        score += 1
        print(f"Correct! Current score: {score}")
        return True
    else:
        print(f"Game over. Final score is: {score}")
        return False

# Game initialization
game_on = True
score = 0

# Randomly select the first player
player_1 = data[randint(0, 49)]

# Display game logo
print(logo)

# Main game loop
while game_on:
    # Randomly select the second player
    player_2 = data[randint(0, 49)]

    # Avoid comparing the same player
    if player_1 == player_2:
        player_2 = data[randint(0, 49)]
        player_1 = data[randint(0, 49)]

    # Retrieve follower counts
    player_1_followers = player_1["follower_count"]
    player_2_followers = player_2["follower_count"]

    # Display players' information
    print(f"Player 1: {player_1['name']}, a {player_1['description']}, from {player_1['country']}.")
    print(vs)
    print(f"Player 2: {player_2['name']}, a {player_2['description']}, from {player_2['country']}.")

    # Prompt user for input
    answer = int(input("Who has more followers? Type 1 or 2: "))

    # Check the answer and update game state
    results = check_answer(answer)
    if results:
        player_1 = player_2
    else:
        game_on = False
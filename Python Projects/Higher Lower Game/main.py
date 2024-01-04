import random
from art import logo, vs
from game_data import data


celeb_num1 = random.randint(0, len(data) - 1)
celeb_num2 = random.randint(0, len(data) - 1)
celeb_num1_followers = data[celeb_num1]["follower_count"]
celeb_num2_followers = data[celeb_num2]["follower_count"]
score = 0


def compare_followers(score):
    if celebrity == 'a' and celeb_num1_followers > celeb_num2_followers:
        score += 1
        print(f"You're right!, Current score: {score}")
        return score

    elif celebrity == 'b' and celeb_num2_followers > celeb_num1_followers:
        score += 1
        print(f"You're right!, Current score: {score}")
        return score
    else:
        clear()
        print(f"You're wrong! Game over! Final score: {score}")
        return False


continue_on = True
while continue_on:
    # Check to see if celebrities are the same before moving on
    if celeb_num1 == celeb_num2:
        celeb_num1 = random.randint(0, len(data) - 1)
        celeb_num2 = random.randint(0, len(data) - 1)
        celeb_num1_followers = data[celeb_num1]["follower_count"]
        celeb_num2_followers = data[celeb_num2]["follower_count"]
    # print logo
    print(logo)

    # Generate 2 celebs to compare
    print("Compare A:", data[celeb_num1]['name'], data[celeb_num1]['description'], data[celeb_num1]['country'])
    print(vs)
    print("Against B:", data[celeb_num2]['name'], data[celeb_num2]['description'], data[celeb_num2]['country'])

    # Ask user for input
    celebrity = input("Who has more followers 'A' or 'B': ").lower()
    clear()

    # Check user selection
    score = compare_followers(score)

    # Continue on or end game base on user selection
    if not score:
        continue_on = False
    else:
        celeb_num1 = celeb_num2
        celeb_num1_followers = celeb_num2_followers
        celeb_num2 = random.randint(0, len(data) - 1)
        celeb_num2_followers = data[celeb_num2]["follower_count"]




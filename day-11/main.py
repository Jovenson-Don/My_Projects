from art import logo
import random
from replit import clear


def start_game():
    your_cards = []
    dealer_cards = []
    game_is_over = False

    # Deal cards to user/dealer
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    # Calculate scores for user and dealer
    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        elif sum(cards) > 21 and len(cards) == 2:
            cards.remove(11)
            cards.append(1)
            return sum(cards)
        else:
            return sum(cards)

    def compare(user_score, dealer_score):
        if user_score == dealer_score:
            print("Draw! Play again!")
        elif user_score == 0:
            print("You win! Blackjack!")
        elif dealer_score == 0:
            print("You lose! Dealer got blackjack")
        elif user_score > 21:
            print("You went over! You lose!")
        elif dealer_score > 21:
            print("Dealer went over! You win!")
        elif user_score > dealer_score:
            print("You win!")
        elif user_score < dealer_score:
            print("You lose!")

    # Start of code
    print(logo)
    for i in range(2):
        your_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_is_over:
        user_score = calculate_score(your_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {your_cards}, current score: {user_score}")
        print(f"Dealer cards: {dealer_cards[0]}")

        if dealer_score == 0 or user_score == 0 or user_score > 21:
            game_is_over = True
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == 'y':
                your_cards.append(deal_card())
            else:
                game_is_over = True

    while dealer_score != 21 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {your_cards} and final score: {user_score}")
    print(f"Dealer final hand: {dealer_cards} and final score: {dealer_score}")
    compare(user_score, dealer_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    start_game()

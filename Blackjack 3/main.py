#The user and computer should each get 2 random cards.
import random
import art

def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Add up the User and Computers scores
def calculate_score(c):
    """Takes a list of cards as input and returns the score"""
    if sum(c) == 21 and len(c) == 2:
        return 0
    elif sum(c) > 21 and 11 in c:
        c.remove(11)
        c.append(1)
    return sum(c)

# Compare the user score and computer score
def compare(user_s, computer_s):
    if user_s > 21 and computer_s > 21:
        return "You went over. You lose 😤"
    if user_s == computer_s:
        return "Draw 🙃"
    elif computer_s == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_s == 0:
        return "Win with a Blackjack 😎"
    elif user_s > 21:
        return "You went over. You lose 😭"
    elif computer_s > 21:
        return "Opponent went over. You win 😁"
    elif user_s > computer_s:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(art.logo)
    # Deal the computer 2 cards each.
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # If the game has not ended, ask the user if they want to draw another card.
            choice = input("Type 'y' for drawing another card. And 'n' to pass.")
            if choice == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    if computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    # Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("SCREEN CLEARED")
    play_game()
import random
from random import choice
from art import logo, vs
from game_data import data

def format(acc):
    account_name = acc['name']
    account_desc = acc['description']
    account_country = acc['country']
    return (f"{account_name}, a {account_desc}, from {account_country}")

def follower(acc):
    follower_count_a = acc['follower_count']
    return follower_count_a

def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        if guess == 'a':
            return True
        else:
            return False
    if b_follower > a_follower:
        if guess == 'b':
            return True
        else:
            return False

score = 0
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format(account_a)}")
    print(vs)
    print(f"Against B: {format(account_b)}")

    choice =input("Which has more followers A or B").lower()

    a_follower_count = follower(account_a)
    b_follower_account = follower(account_b)
    is_correct = check_answer(choice,a_follower_count, b_follower_account)

    print("SCREEN CLEARED")
    print(logo)

    if is_correct:
        score += 1
        print(f"Youre correct {score}")
    else:
        print(f"Youre wrong. final score {score}")
        game_should_continue = False


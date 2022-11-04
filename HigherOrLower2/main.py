#1) print the format - DONE
#2) Get the account name, description, country - DONE
#3) get a random value from the list and assign it to account A and account B - DONE
#4) get the follower count - DONE
#5) create a function to compare the follower count with choice and return true - DONE
#6) If A > B replace B with A - DONE
#7) Place it in a while loop so it keeps repeating - DONE

import random
from art import logo,vs
from game_data import data

def random_no_generator(acc):
    return random.choice(acc)

def format(acc):
    account_name = acc["name"]
    account_desc = acc["description"]
    account_country = acc["country"]
    return (f"{account_name}, a {account_desc}, from {account_country}")

def follower_count(acc):
    account_follower_count = acc["follower_count"]
    return account_follower_count

score = 0
game_over = False

def compare(guess):
    if (follower_count(accountA)) > follower_count(accountB):
        if guess == 'a':
            return True
        else:
            return False
    if follower_count(accountB) > follower_count(accountA):
        if guess == 'b':
            return True
        else:
            return False

accountB = random_no_generator(data)
while game_over == False:
    accountA = accountB
    accountB = random_no_generator(data)
    print(format(accountA))
    print(vs)
    print(format(accountB))
    choice = input("Which has more followers: A or B").lower()
    value = compare(choice)

    if value == True:
        score += 1
        print("You got it correct")
    else:
        print("game over")
        game_over = True
    print(score)







import random
import art
print(art.logo)

def random_no():
    no = random.randint(1,100)
    return no

def guess_game(n, d):
    is_running = False
    while is_running != True and d != 0:
        guess = int(input("Enter the number to be guessed: "))
        if guess < n:
            print("Too Low")
            d = d - 1
            print(f"Attempts left : {d}")
        elif guess > n:
            print("Too High")
            d = d - 1
            print(f"Attempts left : {d}")
        else:
            print(f"You Guessed right, the answer was {n}")
            is_running = True
    if d == 0:
        print("Oops!, you ran out of attempts.")

def difficulty():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    choice = input("Choose a difficulty: Type 'easy' or 'hard':")
    if choice == 'easy':
        return 10
    elif choice == 'hard':
        return 5

number = random_no()
attempt = difficulty()
guess_game(number, attempt)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
coins = {
    "quarter": 1,
    "dimes": 1,
    "nickels": 1,
    "pennies": 1

}
profit = 0

# TODO: 1. Prompt user by asking What would you like? (espresso/latte/cappuccino):
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 3. Print report.
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.

def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return (f"Water : {water}, Milk : {milk}, Coffee : {coffee}, Profit : {profit}")

def calculate_coins():
    for value in coins:
        coins[value] = int(input(f"Enter the no of {value}"))
    amount = coins["quarter"] * 0.25 + coins["dimes"] * 0.10 + coins["nickels"] * 0.05 + coins["pennies"] * 0.01
    return amount

def is_resource_sufficient(d):
    for value in d:
        if d[value] <= resources[value]:
            print(f"{value} : {d[value]} is sufficient")
        else:
            print(f"{value} : {d[value]} is NOT sufficient")
            return True

def check_transaction(a, p):
    if a < cost:
        print("Sorry that's not enough money. Money refunded")
        exit()
    elif a >= cost:
        p += cost
        change = round(a - cost, 2)
        print(f"Heres your change, {change}")
        return p

def make_coffee(d):
    for value in d:
        resources[value] -= d[value]

is_running = False
while not is_running:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        print("Machine Turned OFF")
        exit()
    elif choice == "report":
        print(report())
    else:
        drink = MENU[choice]
        cost = drink["cost"]
        if is_resource_sufficient(drink["ingredients"]) != True:
            amount = calculate_coins()
            profit = check_transaction(amount, profit)
            make_coffee(drink["ingredients"])






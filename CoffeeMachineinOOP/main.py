from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MenuObject = Menu()
CoffeeMakerObject = CoffeeMaker()
MoneyMachineObject = MoneyMachine()
is_running = True

while is_running:
    items = MenuObject.get_items()
    print(items)
    choice = input("What do you want? ").lower()
    if(choice== "off"):
        print("MACHINE OFF")
        exit()
    elif (choice == "report"):
        CoffeeMakerObject.report()
        MoneyMachineObject.report()
    else:
        drink = MenuObject.find_drink(choice)
        if CoffeeMakerObject.is_resource_sufficient(drink):
            if MoneyMachineObject.make_payment(drink.cost):
                CoffeeMakerObject.make_coffee(drink)
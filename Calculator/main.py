import art
print(art.logo)

#Calculator

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div
}
def calculate():
    num1 = float(input("Whats the first number"))

    choice = 'y'
    while(choice == 'y'):
        for i in operations:
            print(i)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("Whats the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start with a new number: ")
        if choice == 'y':
            num1 = answer
        else:
            calculate()

calculate()

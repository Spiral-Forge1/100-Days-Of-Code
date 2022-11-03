print("Welcome to the tip calculator")
bill = round(float(input("What was the total bill? $")),2)

percentage = input("What percentage tip would you like to give? 10, 12, or 15?")
percentage_calculator = bill + (bill * float(percentage)/ 100)

people = input("How many people to split the bill?")
split = percentage_calculator / float(people)
final_amount = "{:.2f}".format(split)

print(f"Each person should pay: ${final_amount}")
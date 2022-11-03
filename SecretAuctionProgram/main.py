import art
print(art.logo)

dictionary1 ={}
input1 = {}
flag = True
def highest(d):
    max1 = 0
    winner = ""
    for i in d:
        if d[i] > max1:
            max1 = d[i]
            winner = i
    print(f"Winner is {winner}, with bid of {max1}")

while flag == True:
    count = 0
    name = input("Enter your name: \n")
    bid = int(input("Enter your bid: $"))
    dictionary1[name] = bid
    print(dictionary1)
    choice = input("Are there other users who wants to bid: y/n\n")
    if choice == 'y':
        print("Screen Cleared")
        flag = True
    else:
        flag = False
        highest(dictionary1)


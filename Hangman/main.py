#Step 3
import random
import word_list
import stages

count = 0
for word in word_list.word_list:
    count = count + 1

random_no = random.randint(0, count)
chosen_word = word_list.word_list[random_no]

print(stages.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create Blanks
word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display += "_"

lives = 6
end_of_game = False
while end_of_game != True:
    guess_any = input("Guess a letter \n")
    guess = guess_any.lower()

    if guess in display:
        print(f"{guess} already in the word")

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"Your letter {guess} not in the word.")
        lives = lives - 1
        print(stages.stages[lives])

    if lives == 0:
        end_of_game = True
        print("You Lose")
        print(f"The word is {str(chosen_word)}")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win")
        print(f"The word is {str(chosen_word)}")
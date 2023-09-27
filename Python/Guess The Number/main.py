#Guess the number

import random

randNum = random.randint(1,10)

easy = 5
hard = 3
attempts = 0

level = input("Enter level (type 'easy' or 'hard') ")
if level == "hard":
    attempts += 3
    print(f"You have {attempts} guesses")

elif level == "easy":
    attempts += 5
    print(f"You have {attempts} guesses")

else:
    print("Invalid level choice. Please type 'easy' or 'hard'.")
    exit()

for i in range(attempts):
    guess = int(input("Enter your guess: "))
    if guess == randNum:
        print("Correct")
        break
    else:
        print("Incorrect")

print(f"You have run out of guesses. the answer is {randNum}")











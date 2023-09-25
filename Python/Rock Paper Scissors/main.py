#Rock Paper Scissors Game

import random


options = ["rock","paper","scissors"]
user_wins = 0
computer_wins = 0

print("Rock Paper Scissors!")
print("Type in rock, paper, scissors or q to quit the game: ")



while True:

    user_input = input("enter rock, paper, scissors or q: ")

    if user_input == 'q':
        break

    if user_input not in options:
        continue
   

    random_number = random.randint(0,2)
    Computer_pick = options[random_number]


    print("The computer chose" , Computer_pick)

    if user_input == computer_wins:
        print("It's a draw!")
    
    elif user_input == "rock" and Computer_pick == "scissors":
        print("You win!")
        user_wins += 1
    
    elif user_input == "paper" and Computer_pick == "rock":
        print("You win!")
        user_wins += 1
    
    elif user_input == "scissors" and Computer_pick == "paper":
        print("You win!")
        user_wins += 1
    
    else:
        print("You lose!")
        computer_wins += 1

print("You won", user_wins, "times")
print("The computer won", computer_wins, "times")

if user_wins > computer_wins:
    print("Well Done!")
else:
    print("Better Luck Next Time")



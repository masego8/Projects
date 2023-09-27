import random
import tkinter as tk
from tkinter import messagebox

# Initialize the game variables
randNum = random.randint(1, 10)
attempts = 0

# Define the function for checking the guess
def check_guess():
    global attempts
    guess = int(entry_guess.get())
    attempts += 1

    if guess == randNum:
        messagebox.showinfo("Result", f"Correct! You guessed the number in {attempts} attempts.")
        reset_game()
    elif guess < randNum:
        messagebox.showinfo("Hint", "Try a higher number.")
    else:
        messagebox.showinfo("Hint", "Try a lower number.")

# Define the function to start a new game
def reset_game():
    global randNum, attempts
    randNum = random.randint(1, 10)
    attempts = 0
    entry_guess.delete(0, tk.END)  # Clear the guess entry field

# Create the main window
root = tk.Tk()
root.title("Guess the Number")

# Create GUI elements
label_intro = tk.Label(root, text="Guess the number between 1 and 10:")
entry_guess = tk.Entry(root)
button_guess = tk.Button(root, text="Guess", command=check_guess)
button_reset = tk.Button(root, text="New Game", command=reset_game)

# Pack GUI elements
label_intro.pack()
entry_guess.pack()
button_guess.pack()
button_reset.pack()

# Start the Tkinter main loop
root.mainloop()

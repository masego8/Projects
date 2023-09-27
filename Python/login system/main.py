import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing Pillow modules

# Global variables
logged_in_username = None

# Function to handle login
def login():
    global logged_in_username
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password are not empty
    if not username or not password:
        messagebox.showerror("Error", "Both username and password are required.")
        return

    # Check if the user exists in the text file
    with open("user_credentials.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_password = line.strip().split(",")
            if username == stored_username and password == stored_password:
                logged_in_username = username
                messagebox.showinfo("Success", f"Welcome, {username}!")
                update_ui_logged_in()
                return

    # If user not found or incorrect password
    messagebox.showerror("Error", "Invalid username or password.")

# Function to handle account creation
def create_account():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password are not empty
    if not username or not password:
        messagebox.showerror("Error", "Both username and password are required.")
        return

    # Check if the username already exists in the text file
    with open("user_credentials.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            stored_username, _ = line.strip().split(",")
            if username == stored_username:
                messagebox.showerror("Error", "Username already exists.")
                return

    # Add the new user to the text file
    with open("user_credentials.txt", "a") as file:
        file.write(f"{username},{password}\n")
        messagebox.showinfo("Success", "Account created!")

# Function to update the UI when a user is logged in
def update_ui_logged_in():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    label_welcome.config(text=f"Welcome, {logged_in_username}!")
    label_username.pack_forget()
    entry_username.pack_forget()
    label_password.pack_forget()
    entry_password.pack_forget()
    button_login.pack_forget()
    button_create_account.pack_forget()
    label_welcome.pack()
    button_logout.pack()

# Function to log out
def log_out():
    global logged_in_username
    logged_in_username = None
    label_welcome.config(text="")
    button_logout.pack_forget()
    label_username.pack()
    entry_username.pack()
    label_password.pack()
    entry_password.pack()
    button_login.pack()
    button_create_account.pack()

# Create the main window
root = tk.Tk()
root.title("Login System")

# Load and display the image
image = Image.open("your_image.png")  # Replace "your_image.png" with your image file
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.image = photo  # This line is important to prevent the image from being garbage collected

# Create GUI elements
label_username = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # Show asterisks for password entry
button_login = tk.Button(root, text="Login", command=login)
button_create_account = tk.Button(root, text="Create Account", command=create_account)
button_logout = tk.Button(root, text="Log Out", command=log_out)
label_welcome = tk.Label(root, text="")

# Pack GUI elements
image_label.pack()  # Display the image
label_username.pack()
entry_username.pack()
label_password.pack()
entry_password.pack()
button_login.pack()
button_create_account.pack()

# Start the Tkinter main loop
root.mainloop()


#Password Generator

import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    username = entry_username.get()
    password_length = int(entry_password_length.get())

    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters)
    for i in range(password_length))

    label_password.config(text=password)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create label and entry for username
label_username = ttk.Label(root, text="Enter user name:")
label_username.grid(column=0, row=0, padx=5, pady=5, sticky='w')
entry_username = ttk.Entry(root)
entry_username.grid(column=1, row=0, padx=5, pady=5)

# Create label and entry for password length
label_password_length = ttk.Label(root, text="Enter password length:")
label_password_length.grid(column=0, row=1, padx=5, pady=5, sticky='w')
entry_password_length = ttk.Entry(root)
entry_password_length.grid(column=1, row=1, padx=5, pady=5)

# Create button and label for generated password
button_generate = ttk.Button(root, text="Generate password", command=generate_password)
button_generate.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
label_password = ttk.Label(root, text="Generated password:")
label_password.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

root.mainloop()

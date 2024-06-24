import random
import secrets
from typing import List
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


letters: List[str] = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers: List[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols: List[str] = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password() -> None:
    try:
        nr_letters = int(entry_letters.get())
        nr_symbols = int(entry_symbols.get())
        nr_numbers = int(entry_numbers.get())

        if nr_letters < 0 or nr_symbols < 0 or nr_numbers < 0:
            raise ValueError("Negative numbers are not allowed.")

        password_list: List[str] = [
            secrets.choice(letters) for _ in range(nr_letters)
        ] + [
            secrets.choice(symbols) for _ in range(nr_symbols)
        ] + [
            secrets.choice(numbers) for _ in range(nr_numbers)
        ]

        random.shuffle(password_list)
        password = ''.join(password_list)
        result_var.set(f"Your secure password is: {password}")

    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

window = tk.Tk()
window.title("PyPassword Generator")
window.geometry("400x300")
window.config(bg="lightblue")

label_intro = tk.Label(window, text="Welcome to the PyPassword Generator!", bg="lightblue", font=("Arial", 14, "bold"))
label_intro.pack(pady=10)

frame = tk.Frame(window, bg="lightblue")
frame.pack(pady=10)

label_letters = tk.Label(frame, text="Number of Letters:", bg="lightblue", font=("Arial", 12))
label_letters.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_letters = ttk.Entry(frame, width=10)
entry_letters.grid(row=0, column=1, padx=10, pady=5)

label_symbols = tk.Label(frame, text="Number of Symbols:", bg="lightblue", font=("Arial", 12))
label_symbols.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_symbols = ttk.Entry(frame, width=10)
entry_symbols.grid(row=1, column=1, padx=10, pady=5)

label_numbers = tk.Label(frame, text="Number of Numbers:", bg="lightblue", font=("Arial", 12))
label_numbers.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_numbers = ttk.Entry(frame, width=10)
entry_numbers.grid(row=2, column=1, padx=10, pady=5)

button_generate = tk.Button(window, text="Generate Password", command=generate_password, bg="darkblue", fg="white", font=("Arial", 12, "bold"))
button_generate.pack(pady=10)

result_var = tk.StringVar()
label_result = tk.Label(window, textvariable=result_var, bg="lightblue", font=("Arial", 12))
label_result.pack(pady=10)

window.mainloop()

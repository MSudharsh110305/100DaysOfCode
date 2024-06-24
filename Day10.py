from tkinter import *
from tkinter import ttk, messagebox
import math

class SuperCalculator(Tk):
    def __init__(self):
        super().__init__()
        self.title("Super Calculator")
        self.geometry("400x600")
        self.configure(bg="#2c3e50")  
        self.resizable(False, False)
        self.memory = None  
        self.create_widgets()  

    def create_widgets(self):
        self.display_var = StringVar()
        self.display = Entry(self, textvariable=self.display_var, font=('Arial', 20), justify='right', bd=10, bg='#ecf0f1')
        self.display.grid(row=0, column=0, columnspan=5, pady=10, padx=10, sticky="nsew")

        button_texts = [
            ("C", 1, 0, 1), ("CE", 1, 1, 1), ("%", 1, 2, 1), ("/", 1, 3, 1),
            ("7", 2, 0, 1), ("8", 2, 1, 1), ("9", 2, 2, 1), ("*", 2, 3, 1),
            ("4", 3, 0, 1), ("5", 3, 1, 1), ("6", 3, 2, 1), ("-", 3, 3, 1),
            ("1", 4, 0, 1), ("2", 4, 1, 1), ("3", 4, 2, 1), ("+", 4, 3, 1),
            ("0", 5, 0, 1), (".", 5, 1, 1), ("(", 5, 2, 1), (")", 5, 3, 1),
            ("sin", 6, 0, 1), ("cos", 6, 1, 1), ("tan", 6, 2, 1), ("√", 6, 3, 1),
            ("=", 7, 0, 4)
        ]

        for (text, row, col, colspan) in button_texts:
            self.create_button(text, row, col, colspan)

        additional_buttons = [
            ("log", 8, 0, 1), ("exp", 8, 1, 1), ("M+", 8, 2, 1), ("MR", 8, 3, 1), ("MC", 8, 4, 1)
        ]

        for (text, row, col, colspan) in additional_buttons:
            self.create_button(text, row, col, colspan)

    def create_button(self, text, row, col, colspan):
        btn = Button(self, text=text, font=('Arial', 15), fg="#fff", bg="#34495e",
                     command=lambda t=text: self.on_button_click(t))
        btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", pady=5, padx=5)

    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "C":
            self.display_var.set("")
        elif char == "CE":
            current_text = self.display_var.get()
            self.display_var.set(current_text[:-1])
        elif char == "√":
            self.calculate_square_root()
        elif char in ["sin", "cos", "tan"]:
            self.calculate_trig_function(char)
        elif char == "log":
            self.calculate_logarithm()
        elif char == "exp":
            self.calculate_exponential()
        elif char == "M+":
            self.memory_store()
        elif char == "MR":
            self.memory_recall()
        elif char == "MC":
            self.memory_clear()
        else:
            self.display_var.set(self.display_var.get() + char)

    def calculate(self):
        try:
            self.display_var.set(eval(self.display_var.get()))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def calculate_square_root(self):
        try:
            self.display_var.set(str(math.sqrt(float(self.display_var.get()))))
        except ValueError:
            messagebox.showerror("Error", "Invalid input for square root")

    def calculate_trig_function(self, func):
        try:
            value = float(self.display_var.get())
            if func == "sin":
                self.display_var.set(str(math.sin(math.radians(value))))
            elif func == "cos":
                self.display_var.set(str(math.cos(math.radians(value))))
            elif func == "tan":
                self.display_var.set(str(math.tan(math.radians(value))))
        except ValueError:
            messagebox.showerror("Error", f"Invalid input for {func}")

    def calculate_logarithm(self):
        try:
            self.display_var.set(str(math.log(float(self.display_var.get()))))
        except ValueError:
            messagebox.showerror("Error", "Invalid input for logarithm")

    def calculate_exponential(self):
        try:
            self.display_var.set(str(math.exp(float(self.display_var.get()))))
        except ValueError:
            messagebox.showerror("Error", "Invalid input for exponential")

    def memory_store(self):
        try:
            self.memory = float(self.display_var.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input for memory store")

    def memory_recall(self):
        if self.memory is not None:
            self.display_var.set(str(self.memory))
        else:
            messagebox.showinfo("Info", "Memory is empty")

    def memory_clear(self):
        self.memory = None
        self.display_var.set("")

if __name__ == '__main__':
    calc = SuperCalculator()
    calc.mainloop()

import tkinter as tk
import math

# --- توابع مثلثاتی بر اساس درجه (نه رادیان) ---
def deg_sin(x):
    return math.sin(math.radians(x))

def deg_tan(x):
    return math.tan(math.radians(x))

# --- منطق ماشین حساب ---
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("ماشین حساب")
        self.root.geometry("360x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e272e")

        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        # نمایشگر
        self.display = tk.Entry(
            self.root,
            font=("Segoe UI", 20),
            bd=0,
            bg="#1e272e",
            fg="#f5f6fa",
            justify="right",
            insertbackground="#f5f6fa"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=16, pady=20, ipady=12, sticky="nsew")

 
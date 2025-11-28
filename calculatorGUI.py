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

        # قاب دکمه‌ها
        btn_frame = tk.Frame(self.root, bg="#1e272e")
        btn_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # تنظیمات ستون‌ها و ردیف‌ها
        for i in range(4):
            btn_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            btn_frame.grid_rowconfigure(i, weight=1)

        # مشخصات دکمه‌ها: متن روی دکمه، مقدار واقعی برای expression، ردیف، ستون، نوع
        buttons = [
            # text, value, row, col, style
            ("C",   "C",    0, 0, "func"),
            ("⌫",   "BACK", 0, 1, "func"),
            ("sin", "sin(", 0, 2, "func"),
            ("tan", "tan(", 0, 3, "func"),

            ("7", "7", 1, 0, "num"),
            ("8", "8", 1, 1, "num"),
            ("9", "9", 1, 2, "num"),
            ("÷", "/", 1, 3, "op"),

            ("4", "4", 2, 0, "num"),
            ("5", "5", 2, 1, "num"),
            ("6", "6", 2, 2, "num"),
            ("×", "*", 2, 3, "op"),

            ("1", "1", 3, 0, "num"),
            ("2", "2", 3, 1, "num"),
            ("3", "3", 3, 2, "num"),
            ("-", "-", 3, 3, "op"),

            ("0", "0", 4, 0, "num"),
            (".", ".", 4, 1, "num"),
            ("=", "=", 4, 2, "equal"),
            ("+", "+", 4, 3, "op"),
        ]

        for (text, value, r, c, kind) in buttons:
            self.create_button(btn_frame, text, value, r, c, kind)

    def create_button(self, frame, text, value, row, col, kind):
        # رنگ‌ها
        bg_num = "#2f3640"
        bg_op = "#273c75"
        bg_func = "#718093"
        bg_equal = "#e1b12c"
        fg_light = "#f5f6fa"

        if kind == "num":
            bg = bg_num
        elif kind == "op":
            bg = bg_op
        elif kind == "func":
            bg = bg_func
        elif kind == "equal":
            bg = bg_equal
        else:
            bg = "#2f3640"

        btn = tk.Button(
            frame,
            text=text,
            font=("Segoe UI", 14),
            bd=0,
            relief="flat",
            bg=bg,
            fg=fg_light,
            activebackground="#40739e",
            activeforeground=fg_light,
            command=lambda v=value: self.on_button_click(v),
            cursor="hand2"
        )
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew", ipady=8)

    def on_button_click(self, value):
        if value == "C":
            self.expression = ""
            self.update_display()
        elif value == "BACK":
            self.expression = self.expression[:-1]
            self.update_display()
        elif value == "=":
            self.calculate()
        else:
            self.expression += value
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate(self):
        try:
            # استفاده از eval با محیط محدود و تعریف sin و tan درجه‌ای
            result = eval(
                self.expression,
                {
                    "__builtins__": None,
                    "sin": deg_sin,
                    "tan": deg_tan,
                    "pi": math.pi,
                    "e": math.e
                },
                {}
            )
            self.expression = str(result)
        except Exception:
            self.expression = "Error"
        self.update_display()

# --- اجرای برنامه ---
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

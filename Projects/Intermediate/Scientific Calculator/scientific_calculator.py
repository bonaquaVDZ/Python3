import ast
import math
import operator as op
import tkinter as tk
from tkinter import messagebox

# Supported operators
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg
}

# Supported functions
functions = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'log': math.log,  # Default base e
    'sqrt': math.sqrt,
    'exp': math.exp,
    'factorial': math.factorial,
    'abs': abs,
    'pi': math.pi,
    'e': math.e,
    'mod': op.mod  # Added modulus function
}


def evaluate_expr(expr):
    """
    Safely evaluate a mathematical expression.
    """
    def _eval(node):
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.Constant):  # For Python 3.8+
            return node.value
        elif isinstance(node, ast.UnaryOp):  # - <number>
            operand = _eval(node.operand)
            return operators[type(node.op)](operand)
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            left = _eval(node.left)
            right = _eval(node.right)
            operator_func = operators[type(node.op)]
            return operator_func(left, right)
        elif isinstance(node, ast.Call):  # Function call
            func_name = node.func.id
            if func_name in functions:
                args = [_eval(arg) for arg in node.args]
                return functions[func_name](*args)
            else:
                raise ValueError(f"Unsupported function '{func_name}'")
        elif isinstance(node, ast.Name):
            if node.id in functions:
                return functions[node.id]
            else:
                raise ValueError(
                    f"Unsupported constant or variable '{node.id}'")
        else:
            raise TypeError(f"Unsupported expression type: {type(node)}")

    try:
        parsed_expr = ast.parse(expr, mode='eval').body
        return _eval(parsed_expr)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.configure(bg="#f0f0f0")  # Set background color to light gray
        master.resizable(False, False)  # Prevent resizing

        # Display widget
        self.display = tk.Entry(
            master,
            width=25,
            font=("Helvetica", 24),
            borderwidth=2,
            relief="groove",
            bg="#ffffff",
            fg="#000000",
            insertbackground="#000000"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

        # Button styles
        self.button_font = ("Helvetica", 18)
        self.button_bg = "#e6e6e6"         # Light gray
        self.button_fg = "#000000"         # Black text
        self.button_active_bg = "#cccccc"  # Darker gray when pressed
        self.button_active_fg = "#000000"  # Black text when pressed

        # Create buttons
        button_texts = [
            ('C', '(', ')', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '.', '%', '='),
            ('sin', 'cos', 'tan', 'log'),
            ('sqrt', 'exp', 'factorial', '**'),
            ('pi', 'e', 'abs', 'mod'),
        ]

        self.buttons = {}
        for r, row in enumerate(button_texts, start=1):
            for c, text in enumerate(row):
                def action(x=text): return self.on_button_click(x)
                btn = tk.Button(
                    master,
                    text=text,
                    width=5,
                    height=2,
                    command=action,
                    font=self.button_font,
                    bg=self.button_bg,
                    fg=self.button_fg,
                    activebackground=self.button_active_bg,
                    activeforeground=self.button_active_fg,
                    relief="raised",
                    borderwidth=2
                )
                btn.grid(row=r, column=c, padx=5, pady=5)
                self.buttons[text] = btn

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            self.calculate_result()
        else:
            current_text = self.display.get()
            new_text = current_text + char
            self.display.delete(0, tk.END)
            self.display.insert(0, new_text)

    def calculate_result(self):
        expr = self.display.get()
        try:
            result = evaluate_expr(expr)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.display.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

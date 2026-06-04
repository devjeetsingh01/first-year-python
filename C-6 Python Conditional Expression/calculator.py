import tkinter as tk
from tkinter import font


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        
        # Display
        self.display_var = tk.StringVar(value="0")
        self.create_display()
        
        # Buttons
        self.create_buttons()
        
        # Internal state
        self.current_input = "0"
        self.operator = None
        self.previous_value = None
        self.should_reset_display = False
    
    def create_display(self):
        """Create the calculator display"""
        display_frame = tk.Frame(self.root, bg="white", relief=tk.SUNKEN, bd=2)
        display_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=False)
        
        display_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 32, "bold"),
            bg="white",
            fg="#333",
            anchor="e",
            padx=10,
            pady=20
        )
        display_label.pack(fill=tk.BOTH, expand=True)
    
    def create_buttons(self):
        """Create calculator buttons"""
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Button layout
        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "←"]
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                self.create_button(button_frame, btn_text, row_idx, col_idx)
    
    def create_button(self, parent, text, row, col):
        """Create individual button"""
        # Determine button styling
        if text in ["÷", "×", "-", "+"]:
            bg_color = "#ff9500"
            fg_color = "white"
            font_obj = font.Font(family="Arial", size=18, weight="bold")
        elif text == "=":
            bg_color = "#34c759"
            fg_color = "white"
            font_obj = font.Font(family="Arial", size=18, weight="bold")
        elif text in ["C", "←"]:
            bg_color = "#ff3b30"
            fg_color = "white"
            font_obj = font.Font(family="Arial", size=16, weight="bold")
        else:
            bg_color = "#e8e8e8"
            fg_color = "#333"
            font_obj = font.Font(family="Arial", size=18, weight="bold")
        
        # Create button
        button = tk.Button(
            parent,
            text=text,
            font=font_obj,
            bg=bg_color,
            fg=fg_color,
            activebackground="#cccccc",
            relief=tk.RAISED,
            bd=2,
            command=lambda: self.on_button_click(text)
        )
        
        # Determine colspan
        colspan = 2 if text in ["0", "C"] else 1
        button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")
    
    def on_button_click(self, char):
        """Handle button clicks"""
        if char in "0123456789":
            self.input_number(char)
        elif char == ".":
            self.input_decimal()
        elif char in ["÷", "×", "-", "+"]:
            self.set_operator(char)
        elif char == "=":
            self.calculate()
        elif char == "C":
            self.clear()
        elif char == "←":
            self.backspace()
    
    def input_number(self, num):
        """Handle number input"""
        if self.should_reset_display:
            self.current_input = num
            self.should_reset_display = False
        else:
            if self.current_input == "0":
                self.current_input = num
            else:
                self.current_input += num
        self.update_display()
    
    def input_decimal(self):
        """Handle decimal point input"""
        if self.should_reset_display:
            self.current_input = "0."
            self.should_reset_display = False
        elif "." not in self.current_input:
            self.current_input += "."
        self.update_display()
    
    def set_operator(self, op):
        """Set operator for calculation"""
        if self.operator is not None and not self.should_reset_display:
            self.calculate()
        
        self.previous_value = float(self.current_input)
        self.operator = op
        self.should_reset_display = True
        self.update_display()
    
    def calculate(self):
        """Perform calculation"""
        if self.operator is None or self.previous_value is None:
            return
        
        try:
            current = float(self.current_input)
            
            if self.operator == "+":
                result = self.previous_value + current
            elif self.operator == "-":
                result = self.previous_value - current
            elif self.operator == "×":
                result = self.previous_value * current
            elif self.operator == "÷":
                if current == 0:
                    self.current_input = "Error"
                    self.update_display()
                    return
                result = self.previous_value / current
            
            # Format result
            if result == int(result):
                self.current_input = str(int(result))
            else:
                self.current_input = str(round(result, 10))
            
            self.operator = None
            self.previous_value = None
            self.should_reset_display = True
            self.update_display()
        except ValueError:
            self.current_input = "Error"
            self.update_display()
    
    def clear(self):
        """Clear calculator"""
        self.current_input = "0"
        self.operator = None
        self.previous_value = None
        self.should_reset_display = False
        self.update_display()
    
    def backspace(self):
        """Remove last digit"""
        if len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
        else:
            self.current_input = "0"
        self.update_display()
    
    def update_display(self):
        """Update display text"""
        self.display_var.set(self.current_input)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

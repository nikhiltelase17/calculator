import tkinter as tk
import pygame

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        # self.geometry("300x400")
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        # Initialize pygame for sound effects
        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("click_effect-86995.mp3")

        self.create_widgets()

    def create_widgets(self):
        # Result Label
        result_label = tk.Label(self, textvariable=self.result_var, font=("Arial", 18), height=2, foreground="green")
        result_label.grid(row=0, column=0, columnspan=5, sticky="e")

        # Buttons
        buttons = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 1, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 2, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 3, 3),
            ("0", 5, 1), ("00", 5, 0), (".", 5, 2), ("=", 5, 3), ("+", 4, 3),
            ("C", 1, 2), ("AC", 1, 0), ("%", 1, 1)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, 
                               text=text, 
                               width=7, 
                               height=2, 
                               command=lambda t=text: self.on_button_click(t), 
                               fg="blue" if text in {"AC", "C", "%", "🔙", "/", "*", "-", "+", "="} else "black")
            button.grid(row=row, column=col, padx=5, pady=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def on_button_click(self, text):
        # Play the click sound
        pygame.mixer.Sound.play(self.click_sound)

        current_result = self.result_var.get()

        if text.isdigit() or text == ".":
            if current_result == "0" or current_result == "Error":
                new_result = text
            else:
                new_result = current_result + text
        elif text == "=":
            try:
                new_result = str(eval(current_result))
            except Exception as e:
                new_result = "Error"
        elif text == "C":
            new_result = current_result[:-1]
        elif text == "AC":
            new_result = "0"
        else:
            new_result = current_result + " " + text + " "

        self.result_var.set(new_result)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()

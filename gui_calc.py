# gui_calc.py
# A simple GUI Calculator built using tkinter

import tkinter as tk  # Import the Tkinter library for GUI development

# Create a Calculator class that inherits from Tk (the main tkinter window)
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Tk)
        self.title("Calculator")         # Set the window title
        self.geometry("300x400")         # Set the window size
        self.resizable(False, False)     # Prevent resizing of the window
        self._expr = ""                  # Store the current expression typed by the user
        self.create_widgets()            # Call method to create all buttons and display

    # Method to create display and buttons
    def create_widgets(self):
        # Create the display entry box
        self.display = tk.Entry(
            self, font=("Arial", 20), borderwidth=2,
            relief="ridge", justify="right"  # Align text to the right
        )
        self.display.pack(fill="both", ipadx=8, ipady=8, padx=10, pady=10)

        # Define button layout (rows of buttons)
        btns = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
        ]

        # Create and pack buttons row by row
        for row in btns:
            frame = tk.Frame(self)  # Create a frame for each row
            frame.pack(expand=True, fill="both")  # Expand frame to fit window width
            for char in row:
                # Create each button and attach its click event
                btn = tk.Button(
                    frame, text=char, font=("Arial", 18),
                    command=lambda ch=char: self.on_press(ch)  # Pass the button text to handler
                )
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

        # Bottom row for "Clear" and "Backspace"
        bottom = tk.Frame(self)
        bottom.pack(expand=True, fill="both")

        # "C" button clears the entire expression
        clr = tk.Button(bottom, text="C", font=("Arial", 18), command=self.clear)
        clr.pack(side="left", expand=True, fill="both", padx=2, pady=2)

        # "⌫" button deletes the last character
        bsp = tk.Button(bottom, text="⌫", font=("Arial", 18), command=self.backspace)
        bsp.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    # Handle button clicks
    def on_press(self, ch):
        if ch == '=':
            try:
                # Evaluate the math expression entered by the user
                # NOTE: eval() is okay here since it's a local calculator
                result = eval(self._expr)
                self._expr = str(result)
            except Exception:
                # If an error occurs (like invalid expression), show "Error"
                self._expr = "Error"
        else:
            # Append the pressed button text to the expression
            self._expr += ch
        self.update_display()  # Update display box with the new expression/result

    # Update the display entry box
    def update_display(self):
        self.display.delete(0, tk.END)      # Clear current content
        self.display.insert(0, self._expr)  # Insert new expression/result

    # Clear the entire display
    def clear(self):
        self._expr = ""          # Empty the expression
        self.update_display()    # Refresh display

    # Delete the last character from the expression
    def backspace(self):
        self._expr = self._expr[:-1]  # Remove the last character
        self.update_display()         # Refresh display

# Run the calculator
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()  # Start the Tkinter main loop (keep window open)

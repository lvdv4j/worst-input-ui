import tkinter as tk
import random

class WorstUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Worst UI - Phone Number Input")

        # Phone number to be entered
        self.phone_number = ''
        
        # Create labels for the moving numbers
        self.labels = []
        for i in range(10):
            label = tk.Label(root, text=str(i), font=('Helvetica', 30))
            label.place(x=random.randint(50, 400), y=random.randint(50, 250))
            self.labels.append(label)
            # Bind the click event for each label to the on_click method
            label.bind('<Button-1>', lambda event, num=i: self.on_click(num))

        # Create a label to display the entered phone number
        self.phone_label = tk.Label(root, text='', font=('Helvetica', 20))
        self.phone_label.place(x=180, y=300)

    def on_click(self, num):
        # Append the clicked number to the phone number
        self.phone_number += str(num)
        # Update the phone number display label
        self.phone_label.config(text=self.phone_number)

    def move_numbers(self):
        # Move the numbers randomly on the screen
        for label in self.labels:
            label.place(x=random.randint(50, 400), y=random.randint(50, 250))
        # Schedule the next movement after 500 milliseconds
        self.root.after(500, self.move_numbers)

if __name__ == "__main__":
    root = tk.Tk()
    worst_ui = WorstUI(root)
    # Start moving the numbers
    worst_ui.move_numbers()
    root.mainloop()

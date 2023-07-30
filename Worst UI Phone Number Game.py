import tkinter as tk
from tkinter import messagebox
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

        # Create a label to display the instructions
        self.instruction_label = tk.Label(root, text='Please enter your phone number:', font=('Helvetica', 16))
        self.instruction_label.place(x=100, y=20)

        # Create a disabled textbox to display the entered phone number
        self.phone_entry = tk.Entry(root, font=('Helvetica', 20), state=tk.DISABLED)
        self.phone_entry.place(x=100, y=60, width=300)

        # Calculate the dimensions to fit all the elements
        width = 500
        height = 350

        # Set the initial size and position of the window
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")

    def on_click(self, num):
        # Append the clicked number to the phone number
        self.phone_number += str(num)
        # Update the phone number display textbox
        self.phone_entry.config(state=tk.NORMAL)
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, self.phone_number)
        self.phone_entry.config(state=tk.DISABLED)

        # Check if the phone number has the required length (e.g., 10 digits)
        if len(self.phone_number) == 10:
            self.show_confirmation()

    def move_numbers(self):
        # Move the numbers randomly on the screen
        for label in self.labels:
            label.place(x=random.randint(50, 400), y=random.randint(50, 250))
        # Schedule the next movement after 500 milliseconds
        self.root.after(500, self.move_numbers)

    def show_confirmation(self):
        response = messagebox.askquestion("Confirmation", f"Is this your number {self.phone_number}?")
        if response == 'yes':
            messagebox.showinfo("Congratulations", "How on earth did you get that right?!")
        else:
            messagebox.showinfo("Try Again", "Try again.")
        # Clear the phone number after the message box is closed
        self.phone_number = ''
        self.phone_entry.config(state=tk.NORMAL)
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    worst_ui = WorstUI(root)
    # Start moving the numbers
    worst_ui.move_numbers()
    root.mainloop()

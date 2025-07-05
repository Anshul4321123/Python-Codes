import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("My Tkinter Window")
root.geometry("300x200")  # width x height

# Function to be called when the button is clicked
def on_button_click():
    messagebox.showinfo("Hello!", "You clicked the button!")

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=50)  # add some vertical padding

# Run the application
root.mainloop()

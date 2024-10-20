
# import the tkinter module 
import tkinter as tk
from tkinter import messagebox

# make the function for adding the two numbers 
def add_numbers():
    # use the try and except for the invalid input
    try:
        # Taking the input numbers from the user
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        # add the two numbers
        result = num1 + num2
        messagebox.showinfo("Result", f"The sum is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter valid numbers.")

# make the function for subtracting the two numbers 
def subtract_numbers():
    # use the try and except for the invalid input
    try:
        # Taking the input numbers from the user
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        # subtract the two numbers
        result = num1 - num2
        messagebox.showinfo("Result", f"The difference is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter valid numbers.")

# make the function for multiplying the two numbers 
def multiply_numbers():
    # use the try and except for the invalid input
    try:
        # Taking the input numbers from the user
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        # multiply the two numbers
        result = num1 * num2
        messagebox.showinfo("Result", f"The product is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter valid numbers.")

# # make the function for clear the level on the GUI 
def clear_entries():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)



# Create the main window
window = tk.Tk()

# Add the Title of the GUI
window.title("BASIC ARITHMETIC CALCULATOR")

# Add the geometry of the GUI
window.geometry("400x200")

# Create the entry fields
entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()

# make the button for the addition
add_button = tk.Button(window, text="ADD", command=add_numbers)
add_button.pack()

# make the button for the subtraction
subtract_button = tk.Button(window, text="SUBTRACT", command=subtract_numbers)
subtract_button.pack()

# make the button for the multiplication
multiply_button = tk.Button(window, text="MULTIPLY", command=multiply_numbers)
multiply_button.pack()

# make the button for the clear the values
clear_button = tk.Button(window, text="CLEAR", command=clear_entries)
clear_button.pack()

# Start the main loop
window.mainloop()

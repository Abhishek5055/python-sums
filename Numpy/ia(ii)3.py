import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    venue = venue_entry.get()
    date_time = date_time_entry.get()
    
    message = f"Thank you {name} for registering for the event."
    messagebox.showinfo("Registration Successful", message)

# Create the main application window
root = tk.Tk()
root.title("Event Registration")

# Set the initial size of the window (width x height)
root.geometry("400x300")  # Change the size as needed

# Create labels and entry widgets for event details
tk.Label(root, text="Event Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Event Venue:").pack()
venue_entry = tk.Entry(root)
venue_entry.pack()

tk.Label(root, text="Date and Time:").pack()
date_time_entry = tk.Entry(root)
date_time_entry.pack()

# Create a Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Start the Tkinter main loop
root.mainloop()

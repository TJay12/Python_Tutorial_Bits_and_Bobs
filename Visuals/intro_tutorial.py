# This **brings in the tkinter module, which is Python's built-in tool kit for making simple windows and buttons.
import tkinter as tk
# Make a small window with tkinter (builtin)
# This creates the main window for your app
window = tk.Tk() # is like saying "open a blank window I can put stuff in."
# window is just a variable name - we use it to control the window later
# Sets the **title bar** of the window to "Hello"
window.title("Hello!")
# Pops up a little window that says "Hi TJ!"
label = tk.Label(window, text="Hi TJ", font=("Arial", 20)) # This creates a label that will be shown inside the window.
# text = "Hi TJ!" is what it will say. font=(Arial, 20) makes it Arial size 20 (can be changed later).
    # window is passed so it knows where to put the label
        # You can change the text, font, or size easily
# This **adds the label to the window**.
    # pack() is one of the simplest ways to lay things out.
label.pack(padx=50, pady=50) # Just give it some space (padding) around the edges.

# This tells Python to keep the window open and listen for interactions (like closing the window).
# It's the main loop of the app - without this, the window would flash and disappear immediatly.
window.mainloop()
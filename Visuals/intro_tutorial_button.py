import tkinter as tk

# Function that changes the label's text when called
def say_hello():
    label.config(text="You're awesome TJ")

window = tk.Tk()
window.title("Hello!")

label = tk.Label(
    window,
    text="Hi TJ",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="darkblue",
    padx=10,
    pady=10
)
label.pack(padx=50, pady=50)

# Button Styling
button = tk.Button(
    window,
    text="Click Me!",
    # tells the button what to do when clicked
    command=say_hello,
    font=("Arial", 16),
    bg="lightgreen",
    fg="black"
)
button.pack(pady=10)

window.mainloop()
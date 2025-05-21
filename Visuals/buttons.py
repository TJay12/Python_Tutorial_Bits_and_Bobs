import tkinter as tk

def say_something():
    label.config(text="You're doing great TJ!", fg="gold", bg="black")

def reset_label():
    label.config(text="Hi TJ", fg="white", bg="darkblue")

window = tk.Tk()
window.title("Style Playground")

label = tk.Label(
    window,
    text="Hi TJ!",
    font=("Comic Sans MS", 24, "bold"),
    fg="white",
    bg="darkblue",
    padx=10,
    pady=10
)
label.pack(padx=50, pady=50)

button1 = tk.Button(
    window,
    text="Compliment Me!",
    command=say_something,
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5
)
button1.pack(pady=5)

button2 = tk.Button(
    window,
    text="Reset",
    command=reset_label,
    font=("Arial", 14),
    bg="#f44336",
    fg="white",
    padx=10,
    pady=5
)
button2.pack(pady=5)

window.mainloop()
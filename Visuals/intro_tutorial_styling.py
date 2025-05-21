import tkinter as tk

window = tk.Tk()
window.title("Hello!")

label = tk.Label(
    window,
    text="Hi TJ",
    font=("Arial", 20, "bold"),
    fg="white",         # Text color (like 'color' in CSS)\
    bg="darkblue",      # background color
    padx=10,            # inner padding
    pady=10
)
label.pack(padx=50, pady=50)

window.mainloop()

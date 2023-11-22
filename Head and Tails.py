import random
import tkinter as tk
from tkinter import messagebox

def heads_or_tails():
    choice = random.choice(["Heads", "Tails"])
    return choice

def flip_coin():
    result = heads_or_tails()
    messagebox.showinfo("Result", f"The coin shows: {result}")

root = tk.Tk()
root.title("Heads or Tails Game")

label = tk.Label(root, text="Welcome to the Heads or Tails game!")
label.pack(pady=20)

flip_button = tk.Button(root, text="Flip Coin", command=flip_coin)
flip_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

root.mainloop()





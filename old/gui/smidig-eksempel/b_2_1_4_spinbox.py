import tkinter as tk
from tkinter import font


def gange():
    try:
        svar = float(tall_1.get()) * float(tall_2.get())
    except ValueError:
        tall_1.delete(0, tk.END)
        tall_2.delete(0, tk.END)
        resultat.configure(text="")
    else:
        resultat.configure(text=f"{svar:.0f}")


root = tk.Tk()
root.title("Spinbox")

default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)

tall_1 = tk.Spinbox(root, from_=0, to=10, increment=1,
                    width=5, font=("Arial 20"))
tall_1.grid(row=0, column=0, padx=10, pady=10)

gangetegn = tk.Label(root, text="*")
gangetegn.grid(row=0, column=1, padx=10, pady=10)

tall_2 = tk.Spinbox(root, from_=0, to=10, increment=1,
                    width=5, font=("Arial 20"))
tall_2.grid(row=0, column=2, padx=10, pady=10)

tk.Button(root, text="=", command=gange, width=5) \
    .grid(row=0, column=3, padx=10, pady=10)

resultat = tk.Label(root, width=5)
resultat.grid(row=0, column=4, padx=10, pady=10)

root.mainloop()

# Smidig IT-2 © TIP AS, 2024

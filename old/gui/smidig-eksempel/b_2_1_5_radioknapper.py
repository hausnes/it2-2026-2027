import tkinter as tk
from tkinter import font


def velg_farge():
    idx_farge = farge_var.get()
    if idx_farge != -1:
        valg.configure(text=farger[idx_farge],
                       fg="white", bg=farger[idx_farge])


root = tk.Tk()
farger = ["red", "blue", "green"]
root.title("Radioknapper")
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=15)
farge_var = tk.IntVar(value=-1)  # Ingen valgt

tk.Label(root, text="Velg farge:", bg="darkgrey", width=20,
      padx=5, pady=5).grid(row=0, column=0, padx=5, pady=5)

for idx, farge in enumerate(farger):
    tk.Radiobutton(root, text=farge, variable=farge_var, value=idx,
                command=velg_farge, width=10, anchor="w") \
        .grid(row=idx + 1, column=0)

valg = tk.Label(root, text="")
valg.grid(row=4, column=0, padx=5, pady=5, sticky="NSEW")

root.mainloop()

# Smidig IT-2 © TIP AS, 2024
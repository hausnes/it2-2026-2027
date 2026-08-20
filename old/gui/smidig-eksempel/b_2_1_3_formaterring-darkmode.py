import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from pathlib import Path

# Funksjon for å vise hilsen basert på inndata
def skriv_ut():
    hilsen.configure(text=f"Hallo {navn.get()}!")

# Opprett et vindu
root = tk.Tk()

# Sett standard font for alle widgets i applikasjonen
root.option_add("*Font", "Arial 20")

# Endre tekst på tittellinjen
root.title("Inndata/Utdata")

# Sett bakgrunnsfarge for vinduet
root.configure(bg="#2e2e2e")

# Legg til et bilde, krever from PIL import Image, ImageTk
bilde = Image.open(Path(__file__).resolve().parent.joinpath("tkinter.jpg"))
# bilde = Image.open("tkinter.jpg")
bilde = bilde.resize((150, 150), Image.Resampling.LANCZOS)
bilde = ImageTk.PhotoImage(bilde)
tk.Label(root, image=bilde, bg="#2e2e2e").grid(row=0, column=0, padx=5, pady=5)

# Lag en ramme for høyre del
frame = tk.Frame(root, padx=10, pady=10, bg="#2e2e2e")
frame.grid(row=0, column=1, padx=5, pady=15)

# navn = tk.Entry(frame, width=15, font=("Arial 20"))
navn = tk.Entry(frame, width=15, bg="#3e3e3e", fg="white", insertbackground="white")
navn.insert(0, "Hva heter du? ")
navn.grid(row=0, column=0, padx=5, pady=13)

tk.Button(frame, text="Les navn", command=skriv_ut, width=10, bg="#5e5e5e", fg="white") \
    .grid(row=0, column=1, padx=5)

hilsen = tk.Label(frame, width=25, bg="#3877ac", fg="white", pady=3)
hilsen.grid(row=1, column=0, columnspan=2, pady=13)

root.mainloop()
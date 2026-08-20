import tkinter as tk            # font er en submodul, 
from tkinter import font        # som ikke kan kalles direkte med tk.
from PIL import Image, ImageTk  # husk pip install Pillow
from pathlib import Path

def si_noe():
    print("Noe!")
    hilsen.configure(text="Hallo du!")

root = tk.Tk()

# Sett standard font for alle widgets i applikasjonen
root.option_add("*Font", "Arial 20")

# Label der det alltid står "Hallo!"
tk.Label(root, text="Hallo!").pack()

# Label-felt der det i utgangspunktet ikke står noe, men som fylles ut av knappen under
hilsen = tk.Label(root)
hilsen.pack()

# Knapp som skriver tekst til hilsen-feltet over
tk.Button(root, text="Trykk på meg!", command=si_noe).pack()

# Legg til et bilde, krever from PIL import Image, ImageTk
bilde = Image.open(Path(__file__).resolve().parent.joinpath("tkinter.jpg"))
# bilde = Image.open("tkinter.jpg") # Alternativ til linje over
bilde = bilde.resize((150, 150), Image.Resampling.LANCZOS)
bilde = ImageTk.PhotoImage(bilde)
tk.Label(root, image=bilde).pack()

root.mainloop()

# Smidig IT-2 © TIP AS, 2024
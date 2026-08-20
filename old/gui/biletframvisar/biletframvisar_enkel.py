import tkinter as tk
from PIL import Image, ImageTk

# Funksjon for å vise bildet
def vis_bilde():
    bilde = Image.open(bilder[bilde_index[0]])
    bilde = bilde.resize((400, 400), Image.Resampling.LANCZOS)
    bilde_tk = ImageTk.PhotoImage(bilde)
    bilde_label.config(image=bilde_tk)
    bilde_label.image = bilde_tk  # Behold referansen til bildet

# Funksjon for å gå til forrige bilde
def forrige_bilde():
    if bilde_index[0] == 0:
        bilde_index[0] = len(bilder) - 1
    else:
        bilde_index[0] -= 1
    vis_bilde()

# Funksjon for å gå til neste bilde
def neste_bilde():
    if bilde_index[0] == len(bilder) - 1:
        bilde_index[0] = 0
    else:
        bilde_index[0] += 1
    vis_bilde()

# Opprett et vindu og sett tittel og størrelse
root = tk.Tk()
root.title("Biletframvisar")
root.geometry("450x550")

# Legg til en overskrift
overskrift = tk.Label(root, text="Biletframvisar", font=("Arial", 24))
overskrift.grid(row=0, column=0, columnspan=2, pady=10)

# Liste over bilder
bilder = [
    "bilde1.jpg",
    "bilde2.jpg",
    "bilde3.jpg"
]
bilde_index = [0]

# Vis det første bildet
bilde = Image.open(bilder[bilde_index[0]])
bilde = bilde.resize((400, 400), Image.Resampling.LANCZOS)
bilde_tk = ImageTk.PhotoImage(bilde)
bilde_label = tk.Label(root, image=bilde_tk)
bilde_label.grid(row=1, column=0, columnspan=2, pady=10, padx=15, sticky="ew")

# Legg til knapper for å navigere mellom bilder
forrige_knapp = tk.Button(root, text="Forrige", command=forrige_bilde)
forrige_knapp.grid(row=2, column=0, pady=10)

neste_knapp = tk.Button(root, text="Neste", command=neste_bilde)
neste_knapp.grid(row=2, column=1, pady=10)

# Start hovedløkken for å holde vinduet åpent
root.mainloop()
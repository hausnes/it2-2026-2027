import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

class App:
    def __init__(self):
        # Opprett et vindu og sett tittel og størrelse
        self.root = tk.Tk()
        self.root.title("Biletframvisar")
        self.root.geometry("450x550")

        # Opprett en hovedramme for applikasjonen
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        # Legg til en overskrift
        self.overskrift = tk.Label(self.frame, text="Biletframvisar", font=("Arial", 24))
        self.overskrift.grid(row=0, column=0, columnspan=2, pady=10)

        # Liste over bilder
        self.bilder = [
            Path(__file__).resolve().parent.joinpath("bilde1.jpg"),
            Path(__file__).resolve().parent.joinpath("bilde2.jpg"),
            Path(__file__).resolve().parent.joinpath("bilde3.jpg")
        ]
        self.bilde_index = 0

        # Vis det første bildet
        self.vis_bilde()

        # Legg til knapper for å navigere mellom bilder
        self.forrige_knapp = tk.Button(self.frame, text="Forrige", command=self.forrige_bilde)
        self.forrige_knapp.grid(row=2, column=0, pady=10)

        self.neste_knapp = tk.Button(self.frame, text="Neste", command=self.neste_bilde)
        self.neste_knapp.grid(row=2, column=1, pady=10)

    def vis_bilde(self):
        # Åpne og vis bildet
        bilde = Image.open(self.bilder[self.bilde_index])
        bilde = bilde.resize((400, 400), Image.Resampling.LANCZOS)
        self.bilde_tk = ImageTk.PhotoImage(bilde)
        if hasattr(self, 'bilde_label'):
            self.bilde_label.config(image=self.bilde_tk)
        else:
            self.bilde_label = tk.Label(self.frame, image=self.bilde_tk)
            self.bilde_label.grid(row=1, column=0, columnspan=2, pady=10, padx=15, sticky="ew")

    def forrige_bilde(self):
        # Gå til forrige bilde
        self.bilde_index = (self.bilde_index - 1) % len(self.bilder)
        self.vis_bilde()

    def neste_bilde(self):
        # Gå til neste bilde
        self.bilde_index = (self.bilde_index + 1) % len(self.bilder)
        self.vis_bilde()

    def run(self):
        # Start hovedløkken for å holde vinduet åpent
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
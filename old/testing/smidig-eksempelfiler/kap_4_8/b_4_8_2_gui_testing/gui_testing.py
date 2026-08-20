# Ved å skille brukergrensesnittet (Gui) fra logikken (App) i programmet,
# forenkler vi gjenbruk, vedlikehold, feilretting og testing av koden.
# Dette gir oss også muligheten til å endre eller erstatte brukergrensesnittet
# uten store endringer i selve logikken.
import tkinter as tk
from tkinter import ttk


class Gui(tk.Tk):
    def __init__(self, app, height=210, width=250):
        super().__init__()
        self.app = app
        self.title("GUI test")
        #center vinduet
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.option_add("*Font", "Arial 16")
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.button = tk.Button(self.frame, text="Klikk meg!",
            command=self.app.on_click)
        self.button.pack(pady=10)

        
        self.farge_valg = tk.StringVar(self, value="Velg farge")
        self.combo = ttk.Combobox(self.frame, textvariable=self.farge_valg,
            values=["Rød", "Grønn", "Blå"], width=8)
        self.combo.pack(pady=10)
        self.farge_valg.trace_add("write", self.endret_farge)
        
        self.label = tk.Label(self.frame, text="Antall klikk: 0")
        self.label.pack(pady=10)

    def endret_farge(self, *args):
        self.app.on_select(self.farge_valg.get())

    def update(self, verdi, type):
        if type == "teller":
            self.label.config(text=f"Antall klikk: {verdi}")
        elif type == "farge":
            self.label.config(text=f"Valgt farge: {verdi}")
class App:
    def __init__(self):
        self.gui = Gui(self)
        self.teller = 0
        self.valgt_farge = None

    def on_click(self):
        self.teller += 1
        self.gui.update(verdi=self.teller, type="teller")

    def on_select(self, farge_valg):
        self.valgt_farge = farge_valg
        self.gui.update(verdi=self.valgt_farge, type="farge")

    def run(self):
        self.gui.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()

# Smidig IT-2 © TIP AS 2024

""" Oppgave 4.8.2 GUI-testing av dennne vær-appen"""

import tkinter as tk
from tkinter import ttk


class Gui(tk.Tk):
    def __init__(self, app, height=100, width=400):
        super().__init__()
        self.app = app
        self.title("Væropp")
        # center vinduet
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.option_add("*Font", "Arial 16")
        style = ttk.Style()
        style.configure("TRadiobutton", font=("Arial", 16))
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.valgt_by = tk.StringVar()
        self.valgt_by.set("")
        self.valgt_by.trace_add("write", self.endret_by)

        self.label = ttk.Label(self.frame, text="Velg by:")
        self.label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=10)

        self.oslo_radio = ttk.Radiobutton(
            self.frame, text="Oslo", variable=self.valgt_by, value="Oslo"
        )
        self.oslo_radio.grid(column=1, row=0, padx=5)

        self.bergen_radio = ttk.Radiobutton(
            self.frame, text="Bergen", variable=self.valgt_by, value="Bergen"
        )
        self.bergen_radio.grid(column=2, row=0, padx=5)

        self.trondheim_radio = ttk.Radiobutton(
            self.frame, text="Trondheim", variable=self.valgt_by, value="Trondheim"
        )
        self.trondheim_radio.grid(column=3, row=0, padx=5)

        self.result_label = ttk.Label(self.frame, text="")
        self.result_label.grid(column=0, row=2, columnspan=4, pady=10)

    def endret_by(self, *args):
        """Kalles når en ny by velges med radioknappene."""
        self.app.on_select(self.valgt_by.get())

    def update(self, by, temperatur):
        """Viser temperaturen for valgt by."""
        tekst = f"Temperaturen i {by} er {temperatur} °C."
        self.result_label.config(text=tekst, foreground='blue')


class App:
    def __init__(self, gui=None):
        # Lar oss sende med en Mock av Gui for enhetstesting av App
        self.gui = gui if gui else Gui(self)
        self.byer = {"Oslo": 20, "Bergen": 15, "Trondheim": 10}
        self.valgt_by = None

    def on_select(self, by_valg):
        """Håndterer valg av by fra GUI."""
        self.valgt_by = by_valg
        try:
            temperatur = self.byer[self.valgt_by]
            self.gui.update(by=self.valgt_by, temperatur=temperatur)
        except KeyError:
            self.gui.update(by=self.valgt_by, temperatur="Ukjent")

    def run(self):
        """Starter hovedløkken i GUI."""
        self.gui.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()

# Smidig IT-2 © TIP AS 2024

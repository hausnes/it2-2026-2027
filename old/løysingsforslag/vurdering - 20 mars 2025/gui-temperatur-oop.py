import tkinter as tk
from tkinter import font

class TemperaturApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Temperaturstyring')
        self.temperatur = 20.0  # Starttemperatur
        self.system_on = True  # Held styr på om systemet er på eller av

        # Konfigurer standard font
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family='Arial', size=15)

        # Opprett GUI-komponentar
        self.create_widgets()

    def create_widgets(self):
        # K1 = Knapp 1 - av/på
        self.K1 = tk.Button(self.root, text='Av/På', bg='#cacaca', command=self.onoff)
        self.K1.grid(row=0, column=0, rowspan=4, sticky='EWNS', padx=(10, 0), pady=10)

        # Opprett ei ramme for displayboksane
        self.display_frame = tk.Frame(self.root, borderwidth=1, relief='solid', padx=5, pady=5)
        self.display_frame.grid(row=1, column=1, columnspan=2, rowspan=2, sticky='NSEW', padx=10, pady=10)

        # D1 = Display, statisk tekst "Temperatur:"
        self.D1 = tk.Label(self.display_frame, text='Temperatur:', font='Arial 20', anchor='center')
        self.D1.grid(row=0, column=0, sticky='EW', pady=(0, 5))

        # D2 = Display, dynamisk tekst "20°C"
        self.D2 = tk.Label(self.display_frame, text=f'{self.temperatur:.1f}°C', font='Arial 20', anchor='center')
        self.D2.grid(row=1, column=0, sticky='EW')

        # K2 = Knapp 2 - temperatur opp
        self.K2 = tk.Button(self.root, text='↑', bg='#cacaca', anchor='center', command=self.temp_up)
        self.K2.grid(row=0, column=3, sticky='EWNS', padx=(0, 10), pady=10)

        # K3 = Knapp 3 - temperatur, sett/bestem
        self.K3 = tk.Button(self.root, text='Sett', bg='#cacaca', anchor='center', command=self.temp_set)
        self.K3.grid(row=1, column=3, rowspan=2, sticky='EWNS', padx=(0, 10))

        # K4 = Knapp 4 - temperatur ned
        self.K4 = tk.Button(self.root, text='↓', bg='#cacaca', anchor='center', command=self.temp_down)
        self.K4.grid(row=3, column=3, sticky='EWNS', padx=(0, 10), pady=10)

        # O = Output/resultat
        self.O = tk.Label(self.root, bg='white', borderwidth=2, relief='sunken', anchor='center')
        self.O.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky='NSEW')

    # Funksjonar som skal knytast til knappane
    def onoff(self):
        # Bytt tilstand mellom på og av
        self.system_on = not self.system_on
        # print(self.system_on)

        if not self.system_on:
            # Slå av visning
            self.D2.config(text="")
            self.O.config(text="Systemet er slått av")
        else:
            # Slå på visning
            self.D2.config(text=f"{self.temperatur:.1f}°C")
            self.O.config(text=f"Temperatur satt til {self.temperatur:.1f}°C")        

    def temp_up(self):
        if self.system_on:  # Berre tillat endring dersom systemet er på
            self.temperatur += 0.5
            self.D2.config(text=f"{self.temperatur:.1f}°C")  # Oppdaterer visninga

    def temp_down(self):
        if self.system_on:  # Berre tillat endring dersom systemet er på
            self.temperatur -= 0.5
            self.D2.config(text=f"{self.temperatur:.1f}°C")  # Oppdaterer visninga

    def temp_set(self):
        if self.system_on:  # Berre tillat endring dersom systemet er på
            self.O.config(text=f"Temperatur satt til {self.temperatur:.1f}°C")  # Oppdaterer resultatboksen


# Opprett hovudvinduet og start applikasjonen
if __name__ == "__main__":
    root = tk.Tk()
    app = TemperaturApp(root)
    root.mainloop()
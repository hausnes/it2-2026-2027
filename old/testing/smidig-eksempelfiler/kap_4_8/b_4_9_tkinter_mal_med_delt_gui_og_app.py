# Ved å skille brukergrensesnittet (Gui) fra logikken (App) i programmet,
# forenkler vi gjenbruk, vedlikehold, feilretting og testing av koden.
# Dette gir oss også muligheten til å endre eller erstatte brukergrensesnittet
# uten store endringer i selve logikken.

import tkinter as tk


class Gui(tk.Tk):
    def __init__(self, app, height=200, width=350):
        super().__init__()
        self.app = app
        self.title("Tkinter-mal med delt GUI og App")
        self.geometry(f"{width}x{height}")
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.button = tk.Button(
            self.frame, text="Trykk meg!", command=self.app.on_click
        )
        self.button.pack(pady=10)

        self.label = tk.Label(self.frame, text="Antall trykk: 0")
        self.label.pack()

    def update(self, teller):
        self.label.config(text=f"Antall trykk: {teller}")


class App:
    def __init__(self):
        self.gui = Gui(self)
        self.teller = 0

    def on_click(self):
        self.teller += 1
        self.gui.update(self.teller)

    def run(self):
        self.gui.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()

# Opphavsrett © TIP AS 2023

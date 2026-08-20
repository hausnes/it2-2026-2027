import tkinter as tk

class App:
    def __init__(self):
        # Opprett et vindu og sett tittel og størrelse
        self.root = tk.Tk()
        self.root.title("Enkel OO-mal for tkinter")
        self.root.geometry("300x200")
        # Opprett en hovedramme for applikasjonen
        self.frame = tk.Frame(self. root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # Opprett en knapp og en label
        self.button = tk.Button(self.frame, text="Trykk meg!", command=self.on_click)
        self.button.pack(pady=10)
        self.label = tk.Label(self.frame, text="Antall trykk: 0")
        self.label.pack()
        # Initialiser telleren
        self.teller = 0

    def on_click(self):
        # Inkrementer telleren og oppdater labelen ved hvert klikk
        self.teller += 1
        self.label.config(text=f"Antall trykk: {self.teller}")

    def run(self):
        # Start hovedløkken for å hold vinduet åpent
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
   
# Smidig IT-2 © TIP AS, 2024
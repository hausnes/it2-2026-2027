"""
Eksempelprogram som viser hvordan en pandas DataFrame kan skrives ut
til en tkinter Text-widget ved bruk av en monospaced font.
"""
import tkinter as tk
import pandas as pd
import platform

df = pd.DataFrame({
    'Navn': ['Knut', 'Tiril', 'Anne', 'Oscar'],
    'Alder': [32, 28, 41, 35]
})


class App:
    def __init__(self):
        '''Vis en pandas.Dataframe som tabell i et tkinter-vindu'''
        self.root = tk.Tk()
        self.root.title("b_3_9_1_monospaced.py")
        self.root.geometry('300x200')
        # Bruk bokstaver med lik bredde på alle plattformer
        if platform.system() == "Windows":
            font = ('Consolas', 18)
        elif platform.system() == "Darwin":  # macOS
            font = ('Menlo', 18)
        else:                                # Linux
            font = ('Monospace', 18)
        # Sett standard skrifttype for alle tkinter-widgeter
        self.root.option_add('*Font', font)
        # Ikke vis indekskolonnen
        tekst = df.to_string(index=False)
        # Legg ut Tekst-widget, sett inn tekst og gjør den skrivebeskyttet
        text_widget = tk.Text(self.root, wrap='none', padx=50, pady=10)
        text_widget.pack(padx=10, pady=10)
        text_widget.insert('1.0', tekst)
        text_widget.configure(state='disabled')

    def run(self):
        '''Start hendelsessløyfen og hold vinduet åpent'''
        self.root.mainloop()


if __name__ == "__main__":
    '''
    Start applikasjonen hvis filen kjøres som et skript.
    Kjøres ikke hvis denne filen importeres som modul.
    '''
    app = App()
    app.run()

# Smidig IT-2 © TIP AS 2024
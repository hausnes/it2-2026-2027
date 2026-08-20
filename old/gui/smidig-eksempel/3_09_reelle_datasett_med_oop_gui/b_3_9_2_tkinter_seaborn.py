import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from matplotlib.backends.backend_tkagg \
import FigureCanvasTkAgg

df = pd.DataFrame({
    'Navn': ['Knut', 'Tiril', 'Anne', 'Oscar'],
    'Alder': [32, 28, 41, 35]
})


class App(tk.Tk):
    def __init__(self):
        '''Viseet Seaborn-diagram i et tkinter-vindu'''
        super().__init__()
        self.title("b_3_9_2_seaborn_tkinter.py")
        self.geometry("800x600")
        self.resizable(False, False)
        sns.set_theme()
        fig, ax = plt.subplots(figsize=(9, 6))
        sns.barplot(data=df, x='Navn', y='Alder')
        fig.suptitle('Seaborn-diagram i tkinter-vindu',
                      fontsize=20)
        ax.set_title('Aldersfordeling')
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def run(self):
        '''Start hendelsessløyfen og hold vinduet åpent'''
        self.mainloop()

    def destroy(self) -> None:
        '''
        Lukk alle matplotlib-figurer og avslutt vinduet.
        Nødvendig når vi bruker matplotlib i tkinter.
        '''
        plt.close('all')
        super().destroy()

if __name__ == "__main__":
    '''
    Start applikasjonen hvis filen kjøres som et skript.
    Kjøres ikke hvis denne filen importeres som modul.
    '''
    app = App()
    app.run()

# Smidig IT-2 © TIP AS 2024
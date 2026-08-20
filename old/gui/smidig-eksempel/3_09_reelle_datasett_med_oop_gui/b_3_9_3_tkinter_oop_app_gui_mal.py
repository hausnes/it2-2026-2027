'''tkinter OOP App GUI Mal'''
import tkinter as tk
from tkinter import ttk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import platform
from tkinter.font import Font


class App:
    def __init__(self):
        '''Opprett en Gui-instans og hent data'''
        self.gui = Gui(self)
        self.df = self.get_data()

    def get_data(self):
        '''Returner data, gjerne fra en fil'''
        return pd.DataFrame({
            'Navn': ['Knut', 'Tiril', 'Anne', 'Oscar'],
            'Alder': [32, 28, 41, 35]
        })

    def handle_request(self, request):
        '''Behandle forespørselen og be gui om å vise resultatet'''
        if request == 'show_table':
            data = self.get_data().sort_values('Alder', ascending=False)
            data = data.to_string(index=False)
            data = f"Personer sortert etter alder:\n\n{data}"
            self.gui.display_text(data)
        elif request == 'show_graph':
            data = self.get_data().copy()
            self.gui.display_graph(data, 'Aldersfordeling')

    def run(self):
        '''Start hendelsessløyfen og hold vinduet åpent'''
        self.gui.mainloop()


class Gui(tk.Tk):
    def __init__(self, app):
        '''opprett GUI-vindu med kontroll- og visningsområder'''
        super().__init__()
        # Lagre en referanse til app-instansen
        self.app = app
        # Vindustittel, størrelse og sentrering
        self.title("Tkinter OOP App GUI Mal")
        b, h = 500, 400
        bs, hs = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f'{b}x{h}+{bs//2-b//2}+{hs//2-h//2}')
        self.resizable(False, False)
        # Bruk skrifttype med lik bredde på alle plattformer
        # for at tabeller skal vises pent med Text-widget
        if platform.system() == "Windows":
            font = ('Consolas', 18)
        elif platform.system() == "Darwin":  # macOS
            font = ('Menlo', 18)
        else:                                # Linux
            font = ('Monospace', 18)
        self.option_add('*Font', font)
        # Kontrollområde for valg av visning
        self.controls_frame = tk.Frame(self, relief='raised', bd=1)
        self.controls_frame.pack(side=tk.TOP, fill='x')
        self.setup_controls()
        # Visnngsområde
        self.display_frame = tk.Frame(self)
        self.display_frame.pack(side=tk.RIGHT, fill='both', expand=True)

    def setup_controls(self):
        '''Opprett kontroller for valg av visning'''
        tk.Button(self.controls_frame, text='Vis Tabell',
                  command=self.show_table_request).grid(
            row=0, column=0, padx=10, pady=10)
        tk.Button(self.controls_frame, text='Vis Graf',
                  command=self.show_graph_request).grid(
            row=0, column=1, padx=10, pady=10)

    def show_table_request(self):
        '''
        Be app om å behandle forespørselen,
        som deretter ber gui om å vise resultatet i en tabell
        '''
        self.app.handle_request('show_table')

    def show_graph_request(self):
        '''
        Be app om å behandle forespørselen,
        som deretter ber gui om å vise resultatet i en graf
        '''
        self.app.handle_request('show_graph')

    def display_text(self, data):
        '''Vis tekst i visningsområdet'''
        self.clear_display_frame()
        # Tekstfelt
        output = tk.Text(self.display_frame, wrap='word')
        output.pack(padx=10, pady=10, fill='both', expand=True)
        # Rullefelt
        scroll = ttk.Scrollbar(output, orient='vertical',
                               command=output.yview)
        scroll.pack(side='right', fill='y')
        output['yscrollcommand'] = scroll.set
        # Tag for marger
        output.tag_configure(
            "marg", lmargin1=10, lmargin2=10, rmargin=10)
        # Tag for fet skrift
        font = Font(output, output.cget("font"))
        font.config(weight="bold")
        output.tag_configure('fet', font=font)
        # Sett inn tekst med fete kolonnenavn
        output.insert('1.0', data, "marg")
        output.tag_add("fet", "3.0", "3.end")
        output['state'] = 'disabled'

    def display_graph(self, data, title):
        '''Vis graf i visningsområdet'''
        self.clear_display_frame()
        sns.set_theme()
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=data, x='Navn', y='Alder', ax=ax)
        ax.set_title(title)
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=self.display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def clear_display_frame(self) -> None:
        '''Fjern alle widgeter fra visningsområdet (før ny visning)'''
        for widget in self.display_frame.winfo_children():
            widget.destroy()

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
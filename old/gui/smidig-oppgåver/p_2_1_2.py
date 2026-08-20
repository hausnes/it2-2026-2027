import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import datetime
from pathlib import Path    


def regn_ut():
    avstand_inn = avstand.get().replace(',', '.')
    fart_inn = fart.get().replace(',', '.')
    try:
        avstand_i_km = float(avstand_inn)
        fart_i_knop = float(fart_inn)
    except ValueError:
        mld = 'FEIL: Oppgi heltall eller desimaltall'
        resultat.configure(text=mld)
    else:
        fart_i_kmpt = fart_i_knop * 1.852
        flytid = avstand_i_km / fart_i_kmpt
        tid = datetime.timedelta(hours=flytid)   # 'hh:mm:ss'
        tid = str(tid).split(':')                # ['hh','mm','ss']
        mld = f'Timer: {tid[0]}, minutter: {tid[1]}, sekunder: {tid[2][:2]}'
        resultat.configure(text=mld)


root = tk.Tk()
root.title('Flytid')
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family='Arial', size=15)
sti = Path(__file__).resolve().parent
fil = sti.joinpath('2_1_hastighetsmaaler.png')
bilde = Image.open(fil)
bilde = bilde.resize((150, 150), Image.Resampling.LANCZOS)
bilde = ImageTk.PhotoImage(bilde)
tk.Label(root, image=bilde).grid(row=0, column=0,
                              rowspan=3, padx=5, pady=5)
tk.Label(text='Avstand i km:', anchor='e', width=12) \
    .grid(row=0, column=1)
tk.Label(text='Fart i knop:', anchor='e', width=12) \
    .grid(row=1, column=1)
tk.Button(text='Regn ut flytid', bg='#cacaca', command=regn_ut) \
    .grid(row=2, column=1, columnspan=2,
          sticky='EW', padx=(0, 10))
avstand = tk.Entry(width=10, font='Arial 15')
avstand.grid(row=0, column=2, padx=10)
fart = tk.Entry(width=10, font='Arial 15')
fart.grid(row=1, column=2, padx=10)
resultat = tk.Label(bg='white', borderwidth=2, relief='sunken')
resultat.grid(row=3, column=0, columnspan=3,
              padx=10, pady=10, sticky='EW')
root.mainloop()

# Smidig IT-2 © TIP AS 2024

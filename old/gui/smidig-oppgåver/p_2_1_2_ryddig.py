import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import datetime  


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

# root-vinduet som me teiknar grafikk til
root = tk.Tk()
root.title('Flytid')
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family='Arial', size=15)

'''
Ei skisse av GUI:

    R = row
    C = column
    B = bilde
    L = label
    E = entry ("input")
    K = knapp
    R = resultat

         C0  C1  C2
    R0    B  L1  E1
    R1    B  L2  E2
    R2    B   K   K
    R3    R   R   R
'''

# B - Bildet
bilde = Image.open("2_1_hastighetsmaaler.png")
bilde = bilde.resize((150, 150), Image.Resampling.LANCZOS)
bilde = ImageTk.PhotoImage(bilde)
bildeLabel = tk.Label(root, image=bilde)
bildeLabel.grid(row=0, column=0, rowspan=3, padx=5, pady=5)

# L1 - Label for avstand
labelAvstand = tk.Label(text='Avstand i km:', anchor='e', width=12)
labelAvstand.grid(row=0, column=1)

# L2 - Label for fart
labelFart = tk.Label(text='Fart i knop:', anchor='e', width=12)
labelFart.grid(row=1, column=1)

# Knappen
knapp = tk.Button(text='Regn ut flytid', bg='#cacaca', command=regn_ut)
knapp.grid(row=2, column=1, columnspan=2, sticky='EW', padx=(0, 10))

# E1 - Inputfelt for avstand
avstand = tk.Entry(width=10, font='Arial 15')
avstand.grid(row=0, column=2, padx=10)

# E2 - Inputfelt for farten
fart = tk.Entry(width=10, font='Arial 15')
fart.grid(row=1, column=2, padx=10)

# R - Tekstfelt for resultatet
resultat = tk.Label(bg='white', borderwidth=2, relief='sunken')
resultat.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='EW')

# Startar mainloop
root.mainloop()
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import datetime  

#------------------------------------------------------------
# Funksjonar som skal knytast til knappane
#------------------------------------------------------------

temperatur = 20.0 # Starttemperatur

def onoff():
    print('On/Off')

# Funksjon for å justere temperaturen opp
def temp_up():
    global temperatur
    temperatur += 0.5
    D2.config(text=f"{temperatur:.1f}°C")  # Oppdaterer visninga

# Funksjon for å justere temperaturen ned
def temp_down():
    global temperatur
    temperatur -= 0.5
    D2.config(text=f"{temperatur:.1f}°C")  # Oppdaterer visninga

# Funksjon for å sette temperaturen
def temp_set():
    O.config(text=f"Temperatur satt til {temperatur:.1f}° C")  # Oppdaterer resultatboksen

#------------------------------------------------------------
# Det grafiske brukargrensesnittet
#------------------------------------------------------------

# root-vinduet som me teiknar grafikk til
root = tk.Tk()
root.title('Temperaturstyring')
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family='Arial', size=15)

'''
Ei skisse av GUI:

    R  = row
    C  = column
    D1  = display statisk tekst "Temperatur:"
    D2  = display dynamisk tekst "20°C"
    K1 = knapp 1 = av/på
    K2 = temperatur opp
    K3 = temperatur, sett/bestem
    K4 = temperatur ned
    O  = Output/resultat

         C0  C1  C2 C3
    R0   K1         K2
    R1   K1  D1  D1 K3
    R2   K1  D2  D2 K3
    R3   K1         K4
    R4    O   O   O  O

    I tillegg så omsluttar ein frame displayboksane D1 og D2
'''

# K1 = Knapp 1 - av/på
K1 = tk.Button(text='Av/På', bg='#cacaca', command=onoff)
K1.grid(row=0, column=0, rowspan=4, sticky='EWNS', padx=(10, 0), pady=10)

# Opprett ei ramme for displayboksane
display_frame = tk.Frame(root, borderwidth=1, relief='solid', padx=5, pady=5)
display_frame.grid(row=1, column=1, columnspan=2, rowspan=2, sticky='NSEW', padx=10, pady=10)

# D1 = Display, statisk tekst "Temperatur:"
D1 = tk.Label(display_frame, text='Temperatur:', font='Arial 20', anchor='center')
D1.grid(row=0, column=0, sticky='EW', pady=(0, 5))

# D2 = Display, dynamisk tekst "20°C"
D2 = tk.Label(display_frame, text='20°C', font='Arial 20', anchor='center')
D2.grid(row=1, column=0, sticky='EW')

# K2 = Knapp 2 - temperatur opp
K2 = tk.Button(text='↑', bg='#cacaca', anchor='center', command=temp_up)
K2.grid(row=0, column=3, sticky='EWNS', padx=(0, 10), pady=10)

# K3 = Knapp 3 - temperatur, sett/bestem
K3 = tk.Button(text='Sett', bg='#cacaca', anchor='center', command=temp_set)
K3.grid(row=1, column=3, rowspan=2, sticky='EWNS', padx=(0, 10))

# K4 = Knapp 4 - temperatur ned
K4 = tk.Button(text='↓', bg='#cacaca', anchor='center', command=temp_down)
K4.grid(row=3, column=3, sticky='EWNS', padx=(0, 10), pady=10)

# O = Output/resultat
O = tk.Label(bg='white', borderwidth=2, relief='sunken', anchor='center')
O.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky='NSEW')

# Startar mainloop
root.mainloop()
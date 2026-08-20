import tkinter as tk
from tkinter import font


def gjør_om():
    tall_inn = dec_tall.get()
    try:
        tall_10 = int(tall_inn)
    except ValueError:
        mld = f'{tall_inn} er ikke et heltall.'
        resultat.configure(text=mld)
    else:
        mld = f'{tall_10} i titallsystemet er {tall_10:b} binært'
        resultat.configure(text=mld)


root = tk.Tk()
root.title('Fra 10- til 2-tallsystemet')
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family='Arial', size=15)

dec_tall = tk.Entry(width=30, font='Arial 15',
                    justify=tk.CENTER)
dec_tall.insert(0, 'Skriv inn et heltall i titallsystemet')
dec_tall.pack(pady=15, padx=15)

tk.Button(text='Gjør om', command=gjør_om, bg='#cacaca') \
    .pack(pady=15)

resultat = tk.Label(width=30, bg='white',
                    borderwidth=2, relief='sunken',)
resultat.pack(padx=15, pady=15)

root.mainloop()

# Smidig IT-2 © TIP AS 2024
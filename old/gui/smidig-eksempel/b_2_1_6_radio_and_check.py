import tkinter as tk
from tkinter import font


def vis_valg():
    if forsikring.get() == 1:
        tekst_ut = ', '.join(
            cb.cget('text')
            for cb, cb_var in zip(avhukingsbokser, avhukings_variabler)
            if cb_var.get()
        )
        tekst_ut = tekst_ut or 'Du har ikke valgt forsikringer'
        valg.configure(text=tekst_ut)
    else:
        valg.configure(text='Du vil ikke ha forsikringer')


def sel_forsikring():
    if forsikring.get() == 1:
        for cb in avhukingsbokser:
            cb.config(state="normal")
        valg.configure(text='Du har ikke valgt forsikringer')
    else:
        for cb in avhukingsbokser:
            cb.config(state="disabled")
            cb.deselect()
        valg.configure(text='Du vil ikke ha forsikringer')


root = tk.Tk()
root.title('Radioknapper og avhukingsbokser')

default_font = font.nametofont("TkDefaultFont")
default_font.configure(family='Arial', size=15)

tk.Label(root, text='Vil du ha forsikring?', bg='darkgrey', padx=5,
         pady=5).grid(row=0, column=0, padx=5, pady=5, sticky='NSEW')

forsikring = tk.IntVar(value=1)
tk.Radiobutton(root, text='Ja', variable=forsikring, value=1,
               command=sel_forsikring, width=10, anchor='w').grid(row=1, column=0)
tk.Radiobutton(root, text='Nei', variable=forsikring, value=0,
               command=sel_forsikring, width=10, anchor='w').grid(row=2, column=0)

tk.Label(root, text='Forsikringstype:', bg='darkgrey', padx=5, pady=5).grid(
    row=0, column=1, padx=5, pady=5, sticky='NSEW')

forsikringer = ['Husforsikring', 'Bilforsikring', 'Helseforsikring']
avhukingsbokser = []
avhukings_variabler = []

for rad, avtale in enumerate(forsikringer, start=1):
    cb_var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=avtale, width=15,
                        anchor='w', variable=cb_var)
    cb.grid(row=rad, column=1)
    avhukingsbokser.append(cb)
    avhukings_variabler.append(cb_var)

tk.Button(root, text='Vis valg', command=vis_valg, borderwidth=3).grid(
    row=4, column=0, columnspan=2, padx=5, pady=5, sticky='NSEW')

valg = tk.Label(root, text='')
valg.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='NSEW')

root.mainloop()

# © TIP AS, 2024
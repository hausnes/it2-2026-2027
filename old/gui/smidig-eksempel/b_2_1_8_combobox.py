import tkinter as tk
from tkinter import ttk

by_data = [["Askim", "Fredrikstad", "Halden", "Moss", "Mysen", "Sarpsborg"],
           [14259, 65415, 25300, 31855, 6513, 45852]]


def oppdater_tekst(*args):
    idx = combobox.current()
    if idx >= 0:  # Sjekker at en gyldig indeks er valgt
        valgt_by = by_data[0][idx]
        innbyggere = by_data[1][idx]
        melding = f"{valgt_by} har {innbyggere} innbyggere."
        tekst_ut.configure(text=melding)


root = tk.Tk()
root.geometry("400x200")
root.title("Combobox")
# Plasser alt i en sentrert ramme
frame = ttk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')
# Label for byvalt
tk.Label(frame, text="Velg by:").grid(row=0, column=0, padx=5, pady=5)
# Opprett Comboboxen
valgt_by = tk.StringVar()
combobox = ttk.Combobox(frame, textvariable=valgt_by,
                        values=by_data[0], state="readonly", width=15)
combobox.grid(row=0, column=1, padx=5, pady=5)
combobox.current(0)  # Setter standardvalg
combobox.configure(height=3)  # for å demonstere rullefelt
valgt_by.trace_add("write", oppdater_tekst)  # Følg med på endringer
# Utdata
tekst_ut = tk.Label(frame, text="")
tekst_ut.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
root.mainloop()

# Smidig IT-2 © TIP AS, 2024
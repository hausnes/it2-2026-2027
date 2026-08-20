import tkinter as tk
from tkinter import font


def vis_valgt_by(_):
    idx = listbox.curselection()[0]
    valgt_by = by_data[0][idx]
    innbyggere = by_data[1][idx]
    melding = f"{valgt_by} har {innbyggere} innbyggere."
    tekst_ut.configure(text=melding)


root = tk.Tk()
root.geometry("400x200")
root.title("Listbox")
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=15)
by_data = [["Askim", "Fredrikstad", "Halden",
            "Moss", "Mysen", "Sarpsborg"],
           [14259, 65415, 25300, 31855, 6513, 45852]]

ramme = tk.Frame(root)
scrollbar = tk.Scrollbar(ramme, orient="vertical")
listbox = tk.Listbox(ramme, height=3, width=10,
                     yscrollcommand=scrollbar.set,
                     selectmode="single")
for by in by_data[0]:
    listbox.insert("end", by)

ramme.pack(pady=25)
scrollbar.configure(command=listbox.yview)
scrollbar.pack(side="right", fill="y")
listbox.pack()
listbox.bind("<<ListboxSelect>>", vis_valgt_by)
tekst_ut = tk.Label(root, text="")
tekst_ut.pack(pady=10)

root.mainloop()

# Smidig IT-2 © TIP AS, 2024
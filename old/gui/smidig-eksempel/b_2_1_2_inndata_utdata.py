import tkinter as tk


def skriv_ut():
    hilsen.configure(text=f"Hallo {navn.get()}!")


root = tk.Tk()

# Opprett widgets
tk.Label(root, text='Hva heter du?').pack()
navn = tk.Entry(root, justify=tk.CENTER)
navn.pack()
navn.focus_set()  # for Mac-brukere
tk.Button(root, text="Les navn", command=skriv_ut).pack()
hilsen = tk.Label(root)
hilsen.pack()

root.mainloop()

# Smidig IT-2 © TIP AS, 2024

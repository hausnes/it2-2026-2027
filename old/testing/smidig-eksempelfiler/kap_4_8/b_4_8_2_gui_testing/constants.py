"""Skriv ut alle tkinter.constants"""

import _tkinter as tkc
import tkinter as tk

print(f"tk.Verson: {tk.TkVersion}")
for constant in  dir(tkc):
    print(constant)


# Smidig IT-2 © TIP AS 2024

'''
Utgangspunkt for dette spelet: 
NRK sitt spel "Tvers": https://www.nrk.no/spill/tvers-1.17073958 

Bli gjerne betre kjent med: https://tkdocs.com/index.html 

Dokumentasjon av deler av programmet i større detalj:
Om box_coords:
    box_coords er ein variabel som inneheld koordinata til ein boks i canvas. Koordinata blir brukt 
    til å sjekke om ein bokstav er plassert innanfor grensene til ein boks når brukaren slepp bokstaven.
    Når du opprettar ein boks i canvas med self.canvas.create_rectangle(...), returnerer metoden ein unik 
    identifikator for boksen. For å få koordinata til boksen, brukar du self.canvas.coords(box), som 
    returnerer ei liste med fire verdier: [x1, y1, x2, y2]. Desse verdiane representerer dei øvre venstre 
    og nedre høgre hjørna til boksen.

Kjelde for ButtonPress-1 osv.: https://www.plus2net.com/python/tkinter-drag-and-drop.php 
'''

import tkinter as tk
import random

class Tvers:
    def __init__(self, root):
        self.root = root
        self.root.title("Tvers")
        self.root.geometry("600x400")

        self.correct_word = "HELLO"
        self.letters = list(self.correct_word)
        random.shuffle(self.letters)

        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        self.boxes = []
        self.letter_labels = []

        self.create_boxes()
        self.create_letters()

    def create_boxes(self):
        for i in range(5):
            box = self.canvas.create_rectangle(100 + i*80, 50, 160 + i*80, 110, fill="white")
            self.boxes.append(box)

    def create_letters(self):
        for i, letter in enumerate(self.letters):
            label = tk.Label(self.root, text=letter, font=("Arial", 24), bg="lightgrey") # 1 stk label per bokstav
            label.place(x=100 + i*80, y=300)
            label.bind("<Button-1>", self.on_drag_start) # Binder venstre museknapp for å starte "drag". # https://www.tcl-lang.org/man/tcl8.6/TkCmd/bind.htm#M11
            label.bind("<B1-Motion>", self.on_drag_motion)  # Flyttar bokstaven medan den blir dratt.
            label.bind("<ButtonRelease-1>", self.on_drag_release) # Binder "slipp" for å sleppe bokstaven.
            self.letter_labels.append(label)

    def on_drag_start(self, event):
        widget = event.widget
        widget.lift()
        self._drag_data = {"x": event.x, "y": event.y}

    def on_drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - self._drag_data["x"] + event.x
        y = widget.winfo_y() - self._drag_data["y"] + event.y
        widget.place(x=x, y=y)

    def on_drag_release(self, event):
        widget = event.widget
        x, y = widget.winfo_x(), widget.winfo_y() # https://www.tcl-lang.org/man/tcl8.6/TkCmd/winfo.htm#M52
        for i, box in enumerate(self.boxes):
            box_coords = self.canvas.coords(box) # Hentar koordintata til boksen
            # Sjekkar om bokstaven sin posisjon er innanfor boksen
            if box_coords[0] < x < box_coords[2] and box_coords[1] < y < box_coords[3]:
                # Sjekkar om boksen er riktig plassert
                if self.correct_word[i] == widget.cget("text"):
                    self.canvas.itemconfig(box, fill="green")
                else:
                    self.canvas.itemconfig(box, fill="red")
                # Plasserer bokstaven i boksen
                widget.place(x=box_coords[0] + 10, y=box_coords[1] + 10)
                return
        # Dersom bokstaven ikkje er plassert i ein boks, returner den til startposisjonen
        widget.place(x=100 + self.letter_labels.index(widget)*80, y=300)

if __name__ == "__main__":
    root = tk.Tk()
    game = Tvers(root)
    root.mainloop()
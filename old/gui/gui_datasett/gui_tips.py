import tkinter as tk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt

# Les CSV-fila og lagre data
def les_csv(filnavn):
    with open(filnavn, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # hopp over header
        data = list(reader)
    return data

data = les_csv('tips.csv')

# Funksjon for å telle antall måltid av ein gitt type
def tell_maltid(maltidstype):
    count = 0
    for row in data:
        if row[5] == maltidstype:
            count += 1
    return count

# Funksjon for å vise antall måltid av kvar type
def vis_antall_maltid():
    dinner_count = tell_maltid('Dinner')
    lunch_count = tell_maltid('Lunch')
    messagebox.showinfo("Antall måltid", f"Det er {dinner_count} måltid av typen 'Dinner'.\nDet er {lunch_count} måltid av typen 'Lunch'.")

# Funksjon for å vise grafisk framstilling av antall måltid
def vis_graf_maltid():
    dinner_count = sum(1 for row in data if row[5] == 'Dinner')
    lunch_count = sum(1 for row in data if row[5] == 'Lunch')
    labels = ['Dinner', 'Lunch']
    sizes = [dinner_count, lunch_count]
    plt.bar(labels, sizes)
    plt.ylabel('Antall måltid')
    plt.xlabel('Måltidstype')
    plt.title('Antall måltid av typen "Dinner" og "Lunch"')
    plt.show()

# Funksjon for å finne og vise største tips
def vis_storste_tips():
    max_tip = 0
    for row in data:
        tip = float(row[1])
        if tip > max_tip:
            max_tip = tip
    messagebox.showinfo("Største tips", f"Den største tipsen som er gitt er {max_tip}.")

# Funksjon for å vise gjennomsnittleg tipsprosent
def vis_gjennomsnittlig_tipsprosent():
    total_bills = [float(row[0]) for row in data]
    tips = [float(row[1]) for row in data]
    total_tip_percentage = sum((tip / total_bill) * 100 for total_bill, tip in zip(total_bills, tips))
    average_tip_percentage = total_tip_percentage / len(total_bills)
    messagebox.showinfo("Gjennomsnittlig tipsprosent", f"Typisk tips utgjer {average_tip_percentage:.2f}% av totalbeløpet.")

# Opprett GUI-vindu
root = tk.Tk()
root.title("Tips Analyse")

# Legg til knapper for forskjellige analyser
btn_antall_maltid = tk.Button(root, text="Vis antall måltid", command=vis_antall_maltid)
btn_antall_maltid.pack(pady=10, padx=10)

btn_graf_maltid = tk.Button(root, text="Vis grafisk framstilling av måltid", command=vis_graf_maltid)
btn_graf_maltid.pack(pady=10, padx=10)

btn_storste_tips = tk.Button(root, text="Vis største tips", command=vis_storste_tips)
btn_storste_tips.pack(pady=10, padx=10)

btn_gjennomsnittlig_tipsprosent = tk.Button(root, text="Vis gjennomsnittlig tipsprosent", command=vis_gjennomsnittlig_tipsprosent)
btn_gjennomsnittlig_tipsprosent.pack(pady=10)

# Start hovedløkka for å halde vindu ope
root.mainloop()
# Sjå tips.ipynb for kode som nyttar Pandas, denne versjonen benyttar kun standardbibliotek.

import csv

with open('tips.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # hopp over header
    data = list(reader)

# Test: Skriv ut første rad
print(data[0])

# Kor mange rader er det i datasettet?
print(f"Det er {len(data)} rader, og derfor like mange måltid som er registrert.")

# Kor mange måltid av typen "dinner" er det?
dinner_count = 0
for row in data:
    if row[5] == 'Dinner':
        dinner_count += 1

print(f"Det er {dinner_count} måltid av typen 'Dinner'.")

# Kor mange måltid av typen "Lunch" er det?
lunch_count = 0
for row in data:
    if row[5] == 'Lunch':
        lunch_count += 1

print(f"Det er {lunch_count} måltid av typen 'Lunch'.")

# Ein grafisk framstilling av kor mange måltid av kvar type som er.
import matplotlib.pyplot as plt

labels = ['Dinner', 'Lunch']
sizes = [dinner_count, lunch_count]
plt.bar(labels, sizes)
plt.ylabel('Antall måltid')
plt.xlabel('Måltidstype')
plt.title('Antall måltid av typen "Dinner" og "Lunch"')
plt.show()

# Kva er den største tipsen som er gitt?
max_tip = 0
for row in data:
    tip = float(row[1])
    if tip > max_tip:
        max_tip = tip

print(f"Den største tipsen som er gitt er {max_tip}.")

# Kor mykje utgjer typisk tipset i prosent av totalbeløpet?
# Lister for å ta vare på totalbeløp og tips
total_bills = []
tips = []

for rad in data:
    total_bills.append(float(rad[0]))  # total_bill er i kolonne 0
    tips.append(float(rad[1]))         # tip er i kolonne 1

# Berekn gjennomsnitteleg tipsprosent
total_tip_percentage = 0
for total_bill, tip in zip(total_bills, tips):
    total_tip_percentage += (tip / total_bill) * 100

average_tip_percentage = total_tip_percentage / len(total_bills)
print(f"Typisk tips utgjer {average_tip_percentage:.2f}% av totalbeløpet.")

# Kjem fleire punkt ..
import csv
import matplotlib.pyplot as plt

# Filsti til CSV-fila
file_path = 'sikkerheit_utf8.csv'

# Liste for å lagre verdiane frå kolonna "Device Information"
device_information = []

# Les CSV-fila manuelt
with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        # Legg til verdien frå kolonna "Device Information" i lista
        device_information.append(row['Device Information'])

# Tell antall forekomster av "Macintosh" og "Windows"
mac_count = 0
win_count = 0
for entry in device_information:
    if entry and "Macintosh" in entry:  # Sjekk at entry ikkje er None eller tom
        mac_count += 1
    elif entry and "Windows" in entry:
        win_count += 1

# Skriv ut resultatene
print(f"Antall angrep på Macintosh: {mac_count}")
print(f"Antall angrep på Windows: {win_count}")

# Visualiser data
plt.bar(['Macintosh', 'Windows'], [mac_count, win_count])
plt.title('Antall angrep per operativsystem')
plt.ylabel('Antall angrep')
plt.xlabel('Operativsystem')
plt.tight_layout()
plt.show()

# Alternativ visualisering - pie
plt.pie(
    [mac_count, win_count], 
    labels=['Macintosh', 'Windows'], 
    autopct='%1.1f%%', 
    colors=['yellow', 'red'], 
    startangle=90
)
plt.title('Fordeling av angrep per operativsystem')
plt.show()
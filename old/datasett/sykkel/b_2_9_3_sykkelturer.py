import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

# sti = Path(__file__).parent.resolve()
# fil = sti.joinpath('05.json')
# sti = Path(__file__).resolve().parent.parent.parent
# fil = sti.joinpath('store_datafiler','05.json')

with open("05.json") as f:
    df = pd.read_json(f)

# print(df.info())

s = df.start_station_name.value_counts()  # Antall turer fra hver startlokasjon
mest_pop = s.head(3)  # De tre mest populære startlokasjonene
minst_pop = s.tail(3)  # De tre minst populære startlokasjonene
s = pd.concat([mest_pop, minst_pop])  # Slå sammen de to seriene

# print(s.iloc[2])
# print(s['Aker Brygge'])
# print(s.index[2])

# Tabell
df_a = s.reset_index()  # Lag en DataFrame av serien
df_a.columns = ['Startlokasjon', 'Antall turer']  # Gi kolonnene andre navn
print('Tre mest og minst populære startlokasjoner')
print(df_a)

# Diagram
sns.set_theme()  # Sett tema for plottet til standard
fig, ax = plt.subplots()  # Nødvendig hvis vi vil endre tittel på vinduet
fig.canvas.manager.set_window_title(
    'b_2_9_3_sykkelturer.py')  # Sett tittel på vinduet
ax = sns.barplot(data=df_a, x='Antall turer', y='Startlokasjon',
                 orient='h')  # Lag horisontalt stolpediagram
ax.set(title='Tre mest og minst populære startlokasjoner') # Sett tittel på plottet
ax.set(xlabel='Antall (Popularitet)', ylabel='Startlokasjon')  # Sett aksetitler
ax.bar_label(ax.containers[0])  # Legg til tallverdier på stolpene
plt.margins(0.15, 0.05)  # Juster marger for å få plass til tallverdiene
plt.tight_layout()  # Juster layout for å få plass til startlokasjonene
plt.show()  # Vis plottet

# Smidig IT-2 © TIP AS, 2024
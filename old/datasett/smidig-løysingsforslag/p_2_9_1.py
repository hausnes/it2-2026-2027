import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import calendar
import locale
locale.setlocale(locale.LC_ALL, 'nb_NO.UTF-8')

# sti = Path(__file__).parent.resolve()
# fil = sti.joinpath('05.json')
# sti = Path(__file__).parent.resolve().parent.parent
# fil = sti.joinpath('store_datafiler','05.json')


with open("05.json") as f:
    df = pd.read_json(f)


s = df.start_station_name.value_counts() # Antall turer fra hver startlokasjon
mest_pop = s.head(3) # De tre mest populære startlokasjonene
minst_pop = s.tail(3) # De tre minst populære startlokasjonene
s = pd.concat([mest_pop, minst_pop]) # Slå sammen de to seriene

# Tabell (oppgave a)
df_a = s.reset_index() # Fra Series til DataFrame
df_a.columns = ['Startlokasjon', 'Antall turer'] # Gi kolonnene navn
print('Tre mest og minst populære startlokasjoner')
print(df_a)

# Diagram (oppgave b)
df['dato'] = pd.to_datetime(df['started_at'])
df['ukedag_nr'] = df['dato'].dt.weekday
s = df.groupby('ukedag_nr').size() # fra DataFrame til Series
s.index = list(calendar.day_name)
sns.set_theme() # Sett tema for plottet til standard
fig, ax = plt.subplots() # Nødvendig hvis vi vil endre tittel på vinduet
fig.canvas.manager.set_window_title('p_2_9_1_sykkelturer.py') # Sett tittel på vinduet
ax = sns.barplot(x=s.index,y=s)
ax.set(title='Antall turer totalt per ukedag')
ax.set(xlabel='', ylabel='Antall turer')
plt.show()
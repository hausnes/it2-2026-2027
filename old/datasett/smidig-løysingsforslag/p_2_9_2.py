import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# sti = Path(__file__).resolve().parent
# fil = sti.joinpath('News_Category_Dataset_v3.json') 
# sti = Path(__file__).parent.resolve().parent.parent
# fil = sti.joinpath('store_datafiler','News_Category_Dataset_v3.json')


df = pd.read_json("News_Category_Dataset_v3.json", lines=True)

# a) 1) Skriv ut antall kategorier
print(f'Antall kategorier: {len(df.category.unique())}')

# a) 2) Skriv ut alle kategoriene
print('\n'.join(df.category.unique()))

# a) 3) Skriv ut de tre mest og minst populære kategoriene
s = df.category.value_counts()
mest_pop = s.head(3)
minst_pop = s.tail(3)
s = pd.concat([mest_pop, minst_pop])
df_1 = s.reset_index()
df_1.columns = ['Kategori', 'Antall artikler']
print('Tre mest og minst populære kategorier')
print(df_1)

# b) Skriv ut forfatterne som har publisert mer enn 2000 artikler.
#    Artikler uten oppgitt forfatter skal ikke tas med.
s = df.authors.value_counts()
forfattere = s[s > 2000]
forfattere = forfattere.drop('')

# c) 1) Lag et stolpediagram med antall artikler per kategori
#       for de 10 største kategoriene
s = df.category.value_counts()
s = s.head(10)
sns.set_theme()
sns.barplot(x=s, y=s.index, orient='h')
plt.title('Antall artikler per kategori')
plt.xlabel('Antall artikler')
plt.ylabel('Kategori')
plt.tight_layout()
plt.show()

# c) 2) Lag et kakediagram over de fem største kategoriene
#       Vis den innbyrdes prosentandel av antall artikler

s = df.category.value_counts()
s = s.head(5)
plt.pie(s, labels=s.index, autopct='%1.1f%%')
plt.title('De fem største kategoriene')
plt.show()
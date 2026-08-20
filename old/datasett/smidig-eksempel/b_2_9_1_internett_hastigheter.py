# NB: Dette eksempelet blir gjennomgått i kapittel 2.8 i læreboka Smidig IT-2.

from pyjstat import pyjstat
import seaborn as sns
import matplotlib.pyplot as plt

# Les data fra URL-en ved hjelp av pyjstat
url = 'https://urban.jrc.ec.europa.eu/api/udp/v2/en/data/?databrick_id=730&nutslevel=0&year=2023'
dataset = pyjstat.Dataset.read(url)

# Konverter datasettet til en pandas DataFrame
df = dataset.write(output='dataframe')
print(df)

# Behold kun kolonnene 'NUTS_CODE' og 'value'
df = df[['NUTS_CODE', 'value']]
df.columns = ['Land', 'Mbps']

# Sorter etter synkende Mbps
df = df.sort_values('Mbps', ascending=False)

# Lag et horisontalt stolpediagram
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Mbps', y='Land', orient='h')
plt.title('Internetthastigheter i EU+EØS+Sveits i 2023')
plt.tight_layout()
plt.show()

# Smidig IT-2 © TIP AS, 2024
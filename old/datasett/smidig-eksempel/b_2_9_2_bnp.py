from pyjstat import pyjstat
import matplotlib.pyplot as plt

url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/tec00001/A.B1GQ.CP_MEUR.DE+ES+FR+IT/?format=JSON&lang=en&startPeriod=2022&endPeriod=2022'
# Bruk eventuelt den nedlasta versjonen av fila over: estat_tec00001_filtered_en.json
ds = pyjstat.Dataset.read(url)
df = ds.write('dataframe')
print(df.head(5)) # Vis de fem første radene
[print(x) for x in df.columns] # Vis kolonnenavn
df = df.iloc[:,[3, 5]] # Velg kolonnene med land og BNP
df.columns = ['Land','BNP'] # Gi kolonnene nye navn
print(df)
labels = ['Tyskland','Spania','Frankrike','Italia'] # Bruk norske navn på landene
plt.suptitle("Størrelsesforhold mellom de 4 største økonomiene i EU")
plt.title("Bruttonasjonalprodukt 2022")
plt.pie(df['BNP'],labels=labels, autopct='%1.0f%%')
plt.show()

# Smidig IT-2 © TIP AS, 2024

'''
NB: Du kan skrive linje 8 slik:
for column in df.columns:
    print(column)
'''
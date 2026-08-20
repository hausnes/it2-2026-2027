'''
    <The Pandas Way>
    Legg merke til bruken av value_counts, head (og potensielt tail)
'''

import pandas
import matplotlib.pyplot as plt

# Last inn fila med nyheiter.
df = pandas.read_json("News_Category_Dataset_v3.json", lines=True)
print(df.columns) # Skriv ut kolonnene i datasettet

# Kor mange saker i kvar kategori?
# Brukar https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.value_counts.html 
print("\nSaker i kvar kategori:")
antall_saker = df['category'].value_counts()
# print(antall_saker)
print(antall_saker.head(5)) # Viser dei forfattarane med flest saker (5)

# Plotting av antall saker i kvar kategori
plt.figure(figsize=(10, 6)) # Dersom du vil endre størrelsen på plottet = ikkje er nøgd med standardstørrelsen
antall_saker.head(5).plot(kind='bar') # NB: Ta vekk .head(5) for å vise alle
plt.xlabel("Kategori")
plt.ylabel("Antall saker")
plt.title("Antall saker i kvar kategori")
plt.xticks(rotation=90)
plt.show()

print("\nSaker per forfattar:")
# Kor mange artiklar har kvar forfattar skrive?
artikkel_teller = df['authors'].value_counts()
# print(artikkel_teller)
artikkel_teller = artikkel_teller.drop('') # Fjern "Ukjent forfattar"
print(artikkel_teller.head(5)) # Viser dei første 5 ...

# Plotting av de 5 mest produktive forfatterne
artikkel_teller.head(5).plot(kind='bar')
plt.xlabel("Forfatter") 
plt.ylabel("Antall artiklar")
plt.title("Dei 5 mest produktive forfattarane")
plt.xticks(rotation=45)
plt.show()

'''
    <The 'manual' way>
'''

# import json
# import matplotlib.pyplot as plt

# # Filnavn
# filnavn = "News_Category_Dataset_v3.json"

# # Ordbok for å telle antall artiklar per forfatter
# artikkel_teller = {}

# # Les JSON-fila linje for linje
# with open(filnavn, encoding="utf-8") as fil:
#     for linje in fil: # Les linje for linje
#         data = json.loads(linje)
#         forfatter = data.get("authors") # Alternativt: data["authors"], fordelen med get er at den returnerer None om nøkkelen ikkje finnes
#         if not forfatter:  # Sjekk for tom streng
#             forfatter = "Ukjent forfattar"
#         if forfatter in artikkel_teller:
#             artikkel_teller[forfatter] += 1
#         else:
#             artikkel_teller[forfatter] = 1

# # Sorter forfattarar etter antall artiklar i synkande rekkefylgje
# sorterte_forfattarar_alle = sorted(artikkel_teller.items(), key=lambda item: item[1], reverse=True)

# # Fjern "Ukjent forfattar" fra listen
# sorterte_forfattarar = []
# for item in sorterte_forfattarar_alle:
#     if item[0] != "Ukjent forfattar":
#         sorterte_forfattarar.append(item)
# # ALternativt:
# # sorterte_forfattarar = [item for item in sorterte_forfattarar if item[0] != "Ukjent forfattar"]

# # Hent ut de 5 mest produktive forfatterne
# topp_5_forfattarar = sorterte_forfattarar[:5]

# # Lag lister for x- og y-aksene
# forfattarar = []
# antall_artiklar = []
# for forfatter, antall in topp_5_forfattarar:
#     forfattarar.append(forfatter)
#     antall_artiklar.append(antall)
# # Alternativt:
# # forfattarar = [forfatter for forfatter, antall in topp_5_forfattarar]
# # antall_artiklar = [antall for forfatter, antall in topp_5_forfattarar]

# # Plotting av de 5 mest produktive forfatterne
# # plt.figure(figsize=(10, 6)) # Dersom du vil endre størrelsen på plottet = ikkje er nøgd med standardstørrelsen
# plt.bar(forfattarar, antall_artiklar, color='skyblue')
# plt.xlabel("Forfatter")
# plt.ylabel("Antall artiklar")
# plt.title("Dei 5 mest produktive forfattarane")
# plt.xticks(rotation=45) # Roterer x-aksen sin tekst 45 grader, forsøk gjerne 90 grader
# plt.subplots_adjust(bottom=0.3)  # Juster margane for å få meir plass under x-aksen, større tal = meir plass, standard er 0.1
# plt.show()
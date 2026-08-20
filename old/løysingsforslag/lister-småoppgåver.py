# Oppgaver for lister i Python, del 1
'''
    Lag en liste med fem tall.
    Legg til et element til listen på slutten.
    Legg til et element til listen på en spesifikk indeks.
    Fjern et element fra listen på en spesifikk indeks.
    Oppdater et element i listen på en spesifikk indeks.
    Finn lengden på listen.
    Slå opp et element i listen basert på indeksen.
    Slå opp et element i listen basert på verdien.
    Sammenlign to lister for likhet.
    Fjern duplikater fra en liste.
    Sorter en liste.
'''

# Lag en liste med fem tall
numbers = [1, 2, 3, 4, 5]

# Legg til et element til listen på slutten
numbers.append(6)

# Legg til et element til listen på en spesifikk indeks
numbers.insert(2, 7)

# Fjern et element fra listen på en spesifikk indeks
numbers.pop(3)

# Oppdater et element i listen på en spesifikk indeks
numbers[1] = 8

# Finn lengden på listen
length = len(numbers)

# Listen etter endringene:
print("Liste med tall:",numbers)

# Slå opp et element i listen basert på indeksen
number = numbers[2]
print("Tallet på indeks 2:",number)

# Slå opp et element i listen basert på verdien
number = numbers.index(7)
print("Indeksen til tallet 7:",number)

# Sammenlign to lister for likhet
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
equal = list1 == list2
print("\nListe 1:",list1)
print("Liste 2:",list2)
print("Listene er like:",equal)

# Fjern duplikater fra en liste
unique_numbers = set(numbers)
print("\nListe med unike tal (etter at den er gjort om til et sett):",unique_numbers)

# Sorter en liste
sorted_numbers = sorted(numbers)
print("\nSortert liste:",sorted_numbers)

# Oppgaver, del 2
'''
    Lag lista verdensdeler som inneholder verdensdelenes navn. Skriv ut den første, midterste og siste verdensdelen i lista. Bruk både positive og negative indekser for å skrive ut verdiene.
    Lag en liste med heltallene fra og med 1 til og med 50. Skriv ut lista for å sjekke at du har fått med de riktige tallene.
    Lag en liste med de første 100 positive oddetallene. Skriv ut lista for å sjekke at du har fått med de riktige tallene.
    Lag en liste som inneholder de første 20 kvadrattallene. Kvadrattall er tall opphøyd i annen, for eksempel 22, 32, osv.
    Lag en liste som inneholder de første 15 kubikktallene. Kubikktall er tall opphøyd i tredje, for eksempel 23, 33, osv.
    Finn ut hva funksjonene min() , max() og sum() gjør. Bruk dem på lister som du har laget i oppgavene ovenfor (lister med tall).
'''

# Lag lista verdensdeler som inneholder verdensdelenes navn. Skriv ut den første, midterste og siste verdensdelen i lista. Bruk både positive og negative indekser for å skrive ut verdiene.
verdensdeler = ["Afrika", "Antarktis", "Asia", "Europa", "Nord-Amerika", "Oseania", "Sør-Amerika"]
print("\nVerdensdelar:",verdensdeler)
print("Første verdensdel:",verdensdeler[0])
print("Midterste verdensdel:",verdensdeler[3])
print("Siste verdensdel:",verdensdeler[-1])

# Lag en liste med heltallene fra og med 1 til og med 50. Skriv ut lista for å sjekke at du har fått med de riktige tallene.
tall = list(range(1, 51))
print("\nHeltall fra 1 til og med 50:",tall)

# Lag en liste med de første 100 positive oddetallene. Skriv ut lista for å sjekke at du har fått med de riktige tallene.
oddetall = list(range(1, 201, 2))
print("\nListe med de første 100 positive oddetala:",oddetall)
# Alternativ løysing:
oddetall = []
i = 1
while len(oddetall) < 100:
    if i % 2 != 0:
        oddetall.append(i)
    i += 1

print("\nAlternativ løysing:",oddetall)

# Lag en liste som inneholder de første 20 kvadrattallene. Kvadrattall er tall opphøyd i annen, for eksempel 22, 32, osv.
kvadrattall = []
for i in range(1, 21):
    kvadrattall.append(i**2)

print("\nListe med de første 20 kvadrattala:",kvadrattall)

# Lag en liste som inneholder de første 15 kubikktallene. Kubikktall er tall opphøyd i tredje, for eksempel 23, 33, osv.
kubikktall = []
for i in range(1, 16):
    kubikktall.append(i**3)

print("\nListe med de første 15 kubikktala:",kubikktall)

# Finn ut hva funksjonene min() , max() og sum() gjør. Bruk dem på lister som du har laget i oppgavene ovenfor (lister med tall).
print("\nMinste verdien i lista med kvadrattall:",min(kvadrattall))
print("Største verdien i lista med kvadrattall:",max(kvadrattall))
print("Summen av alle verdiane i lista med kvadrattall:",sum(kvadrattall))

# Sjekkar om den innebygde funksjonen sum() gjorde jobben rett:
summen = 0
for i in kvadrattall:
    summen += i

print("Summen av alle verdiane i lista med kvadrattall (sjekk):",summen)

# Finn ut om den innebygde funksjonen sum() gjorde jobben raskare enn den me skreiv sjølv! Du kan til dømes bruke modulen time, eller timeit.

# Oppgaver, del 3
# Lag et program som bruker en løkke for å fjerne alle forekomster av tallet 3 fra denne lista: 
liste = [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]
# Fjern alle forekomster av tallet 3 fra lista.
while 3 in liste:
    liste.remove(3)

print("\nListe etter at alle forekomstane av tallet 3 er fjerna:",liste)

# Liste med eksempeltekst
liste = ["Asterix","Obelix","Idefix"]
kopiLliste = list(liste) # Kopierer lista
print("\nListe:",liste)

# ALternativ løysing:
kopiLliste2 = []
for i in liste:
    kopiLliste2.append(i)

print("Kopi av liste:",kopiLliste2)

# Multidimensjonale lister
tabell = [
  ["A", "B", "C"],
  ["D", "E", "F"],
  ["G", "H", "I"]
]
print("\nMultidimensjonal liste:",tabell)
print(tabell[0][1]) # Skriv ut B
listeDagar = ["Måndag","Tysdag","Onsdag","Torsdag","Fredag","Laurdag","Søndag"]
listeVerOgVind = [] # Skal innehalde ei oversikt over dagar og tilhøyrande verobservasjonar

for x in listeDagar:
    print("Innlesing for",x + ":")
    regnmengde = int(input("Regnmengde (mm): "))
    vindstyrke = int(input("Vindstyrke (m/s): "))
    temperatur = int(input("Temperatur (C): "))
    listeVerOgVind.append([x,regnmengde,vindstyrke,temperatur])
print("Utskrift av liste med alle data etter innlesing:",listeVerOgVind)
print("-------------------")

# Liten utvidelse av oppgåve 2.2 a)

for dag in listeVerOgVind: # Tungvint måte med abs. ref. til tal
    print("Dag:",dag[0])
    print("Regnmengde (mm):",dag[1])
    print("vindstyrke (m/s):",dag[2])
    print("Temperatur (C):",dag[3])
    print("-------------------")

'''
Oppgåve 2.2 b)
'''
regnListe = []
vindListe = []
tempListe = []

for dag in range(0,len(listeVerOgVind)):
    regnListe.append(listeVerOgVind[dag][1])
    vindListe.append(listeVerOgVind[dag][2])
    tempListe.append(listeVerOgVind[dag][3])

def regnUtGjennomsnittsverdi(listeInn,typeData):
    totalen = 0
    antall = len(listeInn)
    for x in listeInn:
        totalen += x
    print("Gjennomsnitt for",typeData,"er",round((totalen/antall),2))

regnUtGjennomsnittsverdi(regnListe,"regnmengde")
regnUtGjennomsnittsverdi(vindListe,"vindstyrke")
regnUtGjennomsnittsverdi(tempListe,"temperatur")

'''
Oppgåve 2.2 c)
'''

vindOver = 10
tempLaagareEnn = 5
regnOver = 1

antallVind = 0
antallTemp = 0
antallRegn = 0

# Ikkje det det blei spurt om, men ein test.
antallVind = sum(i > vindOver for i in vindListe)
print("Dagar med vind over",vindOver," m/s er:",antallVind)
antallTemp = sum(i < tempLaagareEnn for i in tempListe)
print("Dagar med temperatur under",tempLaagareEnn," C er:",antallTemp)
antallRegn = sum(i > regnOver for i in regnListe)
print("Dagar med regnmengde over",regnOver,"er:",antallRegn)

# Oppretter lister for å ta vare på dagane som oppfyller krava til ting me ser etter
listeVindOver = []
listeTempLaagare = []
listeRegnOver = []

for i in range(0,7):
    if listeVerOgVind[i][1] > regnOver:
        listeRegnOver.append(listeVerOgVind[i][0])
    if listeVerOgVind[i][2] > vindOver:
        listeVindOver.append(listeVerOgVind[i][0])
    if listeVerOgVind[i][3] < tempLaagareEnn:
        listeTempLaagare.append(listeVerOgVind[i][0])

print("Det regna meir enn",regnOver,"mm fylgjande dagar:",", ".join(listeRegnOver))
print("Det blas meir enn",vindOver,"m/s fylgjande dagar:",", ".join(listeVindOver))
print("Det var kaldare enn",tempLaagareEnn,"C fylgjande dagar:",", ".join(listeTempLaagare))
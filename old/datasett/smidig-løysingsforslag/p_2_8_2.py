import json
personer = []

while True:
    print('Tast bare retur (blankt) for å avslutte')

    navn = input('Skriv inn navnet: ')
    if navn=='':break

    tekst = input('Skriv inn alderen: ')
    if tekst.isnumeric():
        alder = int(tekst)
        personer.append({'navn':navn,'alder':alder})
    elif tekst == '':
        break
    else:
        print(f'{tekst} er ikke et heltall')

with open ('p_2_8_2.json','w',encoding='utf-8') as fil:
    json.dump(personer, fil, ensure_ascii=False, indent=2)

print('Inntasting er skrevet til fil. Sjekk innholdet i p_2_8_2.json')
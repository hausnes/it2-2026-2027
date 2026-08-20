# total = 3 + 'feil'    # Semantisk feil: meningsløst å addere et tall med en tekst.

print('Når du er ferdig med å skrive inn tall,')
print('kan du trykke Enter uten å skrive noe.')
antall_tall = 0

while True:
    tekst_inn = input('Skriv inn et helttall: ')
    try:
        tall = int(tekst_inn)
        print(f'Du skrev inn {tall}')
        antall_tall += 1
    except ValueError:
        print(f'{tekst_inn} er ikke et heltall.')
    finally:
        if tekst_inn == '':
            break

print(f'Du skrev inn {antall_tall} tall.')
print('Takk for nå')

# try:
#     fil = open('eksister.ikke')
# except Exception as unntak:
#     print(f'Type unntak: {unntak.__class__.__name__}')
#     print(unntak)

# Smidig IT-2 © TIP AS, 2024

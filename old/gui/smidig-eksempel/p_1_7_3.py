while True:
    tekst = input('Skriv inn et heltall: ')

    if tekst == 'slutt':
        print('\nTakk for nå.')
        break

    try:
        tall = int(tekst)
    except ValueError:
        print(f'{tekst} er ikke et heltall.')
    else:
        print(f'{tall} i titallsystemet er {tall:b} binært.')
    finally:
        print('\nVi fortsetter. Skriv "slutt" for å avslutte.')

# Smidig IT-2 © TIP AS, 2024
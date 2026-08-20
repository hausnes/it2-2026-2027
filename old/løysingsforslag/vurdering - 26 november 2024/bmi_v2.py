def les_float(prompt):
    while True:
        tekst = input(prompt)
        if tekst == '':
            return None
        try:
            return float(tekst)
        except ValueError:
            print('Input må være et tall.')

def kalkuler_bmi(hoyde_cm, vekt):
    hoyde_m = hoyde_cm / 100
    bmi = vekt / hoyde_m**2
    return bmi

def main():
    print('BMI-kalkulator')

    while True:
        hoyde_cm = les_float('Høyde i cm: ')
        if hoyde_cm is None:
            print('Takk for nå!')
            break

        vekt = les_float('Vekt i kg: ')
        if vekt is None:
            print('Takk for nå!')
            break

        bmi = kalkuler_bmi(hoyde_cm, vekt)
        if bmi < 18.5:
            print(f'bmi = {bmi:.1f} (undervektig)')
        elif bmi < 25:
            print(f'bmi = {bmi:.1f} (normalvektig)')
        else:
            print(f'bmi = {bmi:.1f} (overvektig)')

'''
if __name__ == "__main__" brukes for å sikre at en bestemt del 
av koden bare kjøres når skriptet kjøres direkte, og ikke når 
det importeres som et modul i et annet skript
'''
if __name__ == "__main__":
    main()
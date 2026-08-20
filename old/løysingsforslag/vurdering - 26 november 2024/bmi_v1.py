print('BMI-kalkulator')

while True:
    tekst = input('Høyde i cm: ')
    
    if tekst == '':
        print('Takk for nå!')
        break
    
    try:
        hoyde_cm = float(tekst)
        vekt = float(input('Vekt i kg: '))
    except ValueError:
        print('Input må være tall.')
    
    else:
        hoyde_m = hoyde_cm / 100
        bmi = vekt/hoyde_m**2
        if bmi<18.5:
            print(f'bmi = {bmi:.1f} (undervektig)')
        elif bmi<25:
            print(f'bmi = {bmi:.1f} (normalvektig)')
        else:
            print(f'bmi = {bmi:.1f} (overvektig)')
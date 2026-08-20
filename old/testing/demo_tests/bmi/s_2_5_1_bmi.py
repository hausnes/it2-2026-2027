def bmi_klassifisering(høyde:float,vekt:float)->str:
    bmi = vekt/høyde**2

    if   bmi<18.5: return 'Undervekt'
    elif bmi<25  : return 'Normalvekt'
    elif bmi<30  : return 'Overvekt'
    elif bmi<35  : return 'Fedme, grad 1'
    elif bmi<40  : return 'Fedme, grad 2'
    else:          return 'Fedme, grad 3'

# Smidig IT-2 © TIP AS 2024
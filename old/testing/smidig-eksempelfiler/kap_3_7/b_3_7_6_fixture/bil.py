# bil.py
class Bil:
    def __init__(self):
        self.motor_status = 'stoppet'

    def start_motor(self):
        self.motor_status = 'startet'

    def stopp_motor(self):
        self.motor_status = 'stoppet'

# Eksempel på bruk av Bil-klassen
if __name__ == '__main__':
    bil = Bil()
    print(f'Motorstatus: {bil.motor_status}')
    bil.start_motor()
    print(f'Motorstatus: {bil.motor_status}')
    bil.stopp_motor()
    print(f'Motorstatus: {bil.motor_status}')


# Smidig IT-2 © TIP AS 2024

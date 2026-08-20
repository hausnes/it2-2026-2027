avstand_i_km = float(input('Oppgi avstand i km: '))
fart_i_knop  = float(input('Oppgi fart i knop: '))
fart_i_kmpt  = fart_i_knop * 1.852
flytid       = avstand_i_km / fart_i_kmpt
print(f'Flytiden er {flytid:.2f} timer.')

# Metode 1
timer        = int(flytid)
minutter     = (flytid-timer)*60
sekunder     = (minutter - int(minutter))*60
print(f'Timer: {int(timer)}, minutter: {int(minutter)}, sekunder: {int(sekunder)}')

# Metode 2
flytid_i_sekunder = flytid * 60 * 60
minutter = flytid_i_sekunder // 60
sekunder = flytid_i_sekunder % 60
timer    = minutter // 60
minutter = minutter % 60
print(f'Timer: {int(timer)}, minutter: {int(minutter)}, sekunder: {int(sekunder)}')

# Metode 3
minutter, sekunder = divmod(flytid_i_sekunder, 60)
timer, minutter = divmod(minutter,60)
print(f'Timer: {int(timer)}, minutter: {int(minutter)}, sekunder: {int(sekunder)}')

# Metode 4
import datetime
tid = datetime.timedelta(hours=flytid) # 'hh:mm:ss'
tid = str(tid).split(':')              # ['hh','mm','ss']
print(f'Timer: {tid[0]}, minutter: {tid[1]}, sekunder: {tid[2][:2]}')

# Smidig IT-2 © TIP AS, 2024
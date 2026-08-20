'''
Oppgåve: Stoppeklokke ("løpetrener")
'''
import time

minutter = 0
sekunder = 0
tideler = 0

try:
	while True:
		### Skriv koden din under denne linjen ###
		for minutt in range(0,60):
			if sekunder>=59: # aukar minutter når sekund blir 60, nullstiller deretter sekunder
				minutter += 1
				sekunder = 0
			for sekund in range(0,60): 
				if tideler>=9: # same logikk som for sekund til minutt, no med tideler til sekund
					sekunder += 1
					tideler = 0
				for tidel in range(0,10):
					tideler += 1
					print(minutt,":",sekund,":",tidel)
					time.sleep(1/10)
### Skriv koden din over denne linjen ###
except KeyboardInterrupt:
	print('Tiden var: ',minutter,":",sekunder,":",tidel,sep="")
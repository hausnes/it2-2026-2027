# Enkelt kakediagram
import matplotlib.pyplot as plt

frukt = {'Eple': 3, 'Banan': 5, 'Appelsin': 2, 'Pære': 1}
plt.pie(frukt.values(), labels=frukt.keys(), autopct='%1.0f%%')
plt.show()

# Smidig IT-2 © TIP AS, 2024

'''
NB: Parameteren autopct bestemmer korleis prosentverdiane skal visast i kakediagrammet.
Dette betyr at prosentverdiane vil bli vist som heiltal utan desimalar, etterfylgt av prosentteiknet. 
'''
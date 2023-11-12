# 1. tehtävä
import random

arpaL = []
summa = 0

arpa_input = int(input('Kirjoita arpakuutioiden lukumäärä: '))

for luku in range(arpa_input):
    arpaL.append(random.randint(1,6))

for i in range(0,len(arpaL)):
    summa = summa + arpaL[i]

print('Arpakuutioiden luvut: ',arpaL)
print(f'Arpakuutioiden määrä on {arpa_input} ja silmälukujen summa on {summa}')
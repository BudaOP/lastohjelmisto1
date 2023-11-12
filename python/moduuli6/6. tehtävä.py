import math

def hinta(cm, e):
    # muutetaan cm to m
    m = cm / 100
    pizzan_a = math.pi * (m / 2)**2                     #jaetaan m / 2, eli halkaisija => säde
    yksikkohinta = e / pizzan_a
    return yksikkohinta


halk1 = float(input('Kirjoita ensimmäisen pizzan halkaisijan senttimetreinä: '))
hinta1 = float(input('Kirjoita ensimmäisen pizzan hinta euroina: '))
halk2 = float(input('Kirjoita toisen pizzan halkaisijan senttimetreinä: '))
hinta2 = float(input('Kirjoita toisen pizzan hinta euroina: '))

pizza1 = hinta(halk1, hinta1)
pizza2 = hinta(halk2, hinta2)

if pizza1 < pizza2:
    print(f'Ensimmäisen pizzan {pizza1:.2f} euroa/m\u00b2 yksikköhinta on alhaisempi kuin toisen pizzan')
else:
    print(f'Toisen pizzan {pizza2:.2f} euroa/m\u00b2 yksikköhinta on alhaisempi kuin ensimmäisen pizzan')
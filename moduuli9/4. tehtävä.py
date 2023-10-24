import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus <= self.huippunopeus and uusi_nopeus >= 0:
            self.nopeus = uusi_nopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka = self.matka + tunnit * self.nopeus

autot = []

# Tehdään rekisteritunnukset ja huippunopeudet
for auto in range(1, 11):
    rekisteritunnus = f'ABC-{auto}'
    huippunopeus = random.randint(100,200)
# Sijoitetaan listaan 10 autoa ja niiden parametrit
    uusi_auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(uusi_auto)

tunnit = 0
loop = True

while loop:
    tunnit += 1

    for auto in autot:
        nopeuden_muutos = random.randint(-10,15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)

    for auto in autot:
        if auto.matka >= 10000:
            loop = False

print('Kilpailun tulokset')
print('Rekisteritunnus   Huippunopeus   Nopeus     Matka\n')
for auto in autot:
    print(f'{auto.rekisteritunnus:16}  {auto.huippunopeus}km/h{auto.nopeus:11}km/h    {auto.matka}km')
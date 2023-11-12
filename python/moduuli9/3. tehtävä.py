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

uusi_auto = Auto("ABC-123", 142)

print(f"Uuden auton ominaisuudet:\nRekisteritunnus: {uusi_auto.rekisteritunnus}"
      f"\nHuippunopeus: {uusi_auto.huippunopeus} km/h\nNopeus nyt: {uusi_auto.nopeus} km/h"
      f"\nKuljettu matka: {uusi_auto.matka} km/h")


# Alkuperäinen nopeus
print(f'\nAuton alkuperäinen nopeus on {uusi_auto.nopeus} km/h. Auto kiihdyttää...')

# +30km
uusi_auto.kiihdyta(30)

# +70km
uusi_auto.kiihdyta(70)

# +50km
uusi_auto.kiihdyta(50)
print(f'Auton uusi nopeus on {uusi_auto.nopeus} km/h')

# Testataan kulje metodia (3h)
uusi_auto.kulje(3)
print(f"Auton kuljettu matka 3 tunnin päästä (100km/h) nopeudella on {uusi_auto.matka}km")

# Hätäjarrutus
uusi_auto.kiihdyta(-200)
print('HÄTÄJARRUTUS!!!')
print(f'Auton uusi nopeus on {uusi_auto.nopeus} km/h')

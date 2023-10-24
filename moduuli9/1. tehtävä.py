class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

uusi_auto = Auto("ABC-123", 142)

print(f"Uuden auton ominaisuudet:\nRekisteritunnus: {uusi_auto.rekisteritunnus}"
      f"\nHuippunopeus: {uusi_auto.huippunopeus} km/h\nNopeus nyt: {uusi_auto.nopeus} km/h"
      f"\nKuljettu matka: {uusi_auto.matka} km/h")

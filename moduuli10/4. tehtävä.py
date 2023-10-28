import random
from prettytable import PrettyTable

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

class Kilpailu:
    def __init__(self, k_nimi, km, osallistujat):
        self.k_nimi = k_nimi
        self.km = km
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        for auto in self.osallistujat:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print('Kilpailun tulokset')
        myTable = PrettyTable(["Rekisteritunnus", "Huippunopeus", "Nopeus", "Matka"])
        for auto in self.osallistujat:
            myTable.add_row([auto.rekisteritunnus, f'{auto.huippunopeus} km/h', f'{auto.nopeus} km/h', f'{auto.matka} km'])
        print(myTable)

    def kilpailu_ohi(self):
        for auto in self.osallistujat:
            if auto.matka >= self.km:
                print(f'\n{auto.rekisteritunnus} pääsi maaliin!')
                return True
        return False

autot = []

# Tehdään rekisteritunnukset ja huippunopeudet
for auto in range(1, 11):
    rekisteritunnus = f'ABC-{auto}'
    huippunopeus = random.randint(100,200)
    # Sijoitetaan listaan 10 autoa ja niiden parametrit
    uusi_auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(uusi_auto)

kilpailu = Kilpailu('Suuri romuralli', 8000, autot)

tunti = 0

while not kilpailu.kilpailu_ohi():
    tunti += 1
    kilpailu.tunti_kuluu()

    if tunti % 10 == 0:
        print(f'Tilanne {tunti} tunnin jälkeen:')
        kilpailu.tulosta_tilanne()

print('gg wp, kilpailu päättyi.')
kilpailu.tulosta_tilanne()
import random
from prettytable import PrettyTable

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta_tiedot(self):
        print(f"Auton rekisteritunnus: {self.rekisteritunnus}\n- Huippunopeus: {self.huippunopeus} km/h")

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus <= self.huippunopeus and uusi_nopeus >= 0:
            self.nopeus = uusi_nopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka = self.matka + tunnit * self.nopeus

class Sahkoauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti_kWh):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akku_kWh = akkukapasiteetti_kWh

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"- Akun kapasiteetti: {self.akku_kWh} kWh")

class Polttomoottoriauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus,bensastankin_kokol):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensastankki = bensastankin_kokol

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"- Bensastankin koko: {self.bensastankki} l")

autot = []

autot.append(Sahkoauto("ABC-15", 180, 52.5))
autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))

for auto in autot:
    auto.kiihdyta(random.randint(40,150))
    auto.kulje(3)
    auto.tulosta_tiedot()
    print(f"- Matkamittarilukema: {auto.matka} km\n")
class Julkaisu:

    julkaisujen_lukumaara = 0

    def __init__(self, j_nimi):
        Julkaisu.julkaisujen_lukumaara = Julkaisu.julkaisujen_lukumaara + 1
        self.julkaisuja = Julkaisu.julkaisujen_lukumaara
        self.j_nimi = j_nimi

    def tulosta_tiedot(self):
        print(f"{self.julkaisuja}. Julkaisu: {self.j_nimi}")


class Kirja(Julkaisu):
    def __init__(self, j_nimi,kirjoittaja, sivut):
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut
        super().__init__(j_nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja} - Sivumäärä: {self.sivut}")

class Lehti(Julkaisu):

    def __init__(self, j_nimi, toimittaja):
        self.toimittaja = toimittaja
        super().__init__(j_nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittajana: {self.toimittaja}")

julkaisut = []
julkaisut.append(Lehti("Aku Ankka",  "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", "200"))

for t in julkaisut:
    t.tulosta_tiedot()
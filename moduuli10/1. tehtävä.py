class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde):
        print(f'Olet tällä hetkellä hississä {self.nykyinen_kerros}. kerroksessa.')
        # Annetaan aluksi rajat
        if kohde < self.alin_kerros:
            print(
                f'Valitsit {kohde}. kerroksen, vaikka alin kerros on {self.alin_kerros}. Siirryt siis alimpaan kerrokseen')
            kohde = self.alin_kerros
        elif kohde > self.ylin_kerros:
            print(
                f'Valitsit {kohde}. kerroksen, vaikka ylin kerros on {self.ylin_kerros}. Siirryt siis ylimpään kerrokseen')
            kohde = self.ylin_kerros

        # itse siirtyminen
        print(f'Valitsit {kohde}. kerroksen\n')
        while self.nykyinen_kerros < kohde:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde:
            self.kerros_alas()
        if self.nykyinen_kerros == kohde:
            print('DING DING!!! Olet valitsemasi kerroksessa.\n')
    def kerros_ylös(self):
        self.nykyinen_kerros = self.nykyinen_kerros + 1
        print(f'Siirryt ylös päin... Kerroksesi on {self.nykyinen_kerros}')

    def kerros_alas(self):
        self.nykyinen_kerros = self.nykyinen_kerros - 1
        print(f'Siirryt alas päin... Kerroksesi on {self.nykyinen_kerros}')

h = Hissi(1,15)

h.siirry_kerrokseen(17)
h.siirry_kerrokseen(-2)
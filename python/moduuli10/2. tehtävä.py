class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde):
        print(f'Olet tällä hetkellä hississä {self.nykyinen_kerros}. kerroksessa.')
        # Annetaan aluksi rajat
        if kohde < self.alin_kerros:
            print(f'Valitsit {kohde}. kerroksen, vaikka alin kerros on {self.alin_kerros}. Siirryt siis alimpaan kerrokseen')
            kohde = self.alin_kerros
        elif kohde > self.ylin_kerros:
            print(f'Valitsit {kohde}. kerroksen, vaikka ylin kerros on {self.ylin_kerros}. Siirryt siis ylimpään kerrokseen')
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

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, h_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.h_lukumaara = []
        self.hissit = []

        for i in range(h_lukumaara):
            self.h_lukumaara.append(i + 1)
        for i in range(h_lukumaara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissi(self, hissi_nro, kohde):
        if hissi_nro in self.h_lukumaara:
            print(f'Valitsit {hissi_nro} hissin.')
            hissi = self.hissit[hissi_nro - 1]
            hissi.siirry_kerrokseen(kohde)
        else:
            print('Ei ole sellaista hissiä!!!')


talo = Talo(1,15,4)
talo.aja_hissi(3,13)
talo.aja_hissi(4,10)
talo.aja_hissi(4,6)
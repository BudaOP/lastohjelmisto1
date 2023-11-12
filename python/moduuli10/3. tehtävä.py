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
            print('DING DING!!!\n')
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

    def aja_hissi(self, hissi_nro, kohde):
        if hissi_nro in self.h_lukumaara:
            print(f'Valitsit {hissi_nro} hissin.')
            self.hissi = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissi.siirry_kerrokseen(kohde)
            self.hissit.append(self.hissi)
            self.h_nro = hissi_nro
        else:
            print('Ei ole sellaista hissiä!!!!!!!!!')

    def palohalytys(self):
        print("HUOMIO!!!\nPALOHÄLYTYS! Kaikki hissit siirretään pohjakerrokseen.")
        for h in self.hissit:
            h.siirry_kerrokseen(self.alin_kerros)

talo = Talo(1,15,4)
talo.aja_hissi(4,14)
talo.aja_hissi(1,10)
talo.aja_hissi(2,12)
talo.aja_hissi(3,13)
talo.palohalytys()
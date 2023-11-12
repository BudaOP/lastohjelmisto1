# 4. tehtävä
vuosi = int(input('Kirjoita vuosiluku: '))

print(vuosi)

karkausvuosiCalc = vuosi / 4
karkausvuosi = karkausvuosiCalc == int(karkausvuosiCalc)

karkausvuosiCalc2 = vuosi / 400
karkausvuosi2 = karkausvuosiCalc2 == int(karkausvuosiCalc2)

if karkausvuosi:
    print(vuosi, 'vuosi on karkausvuosi')
else: print(vuosi, 'ei ole karkausvuosi')
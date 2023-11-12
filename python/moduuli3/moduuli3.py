# 1. tehtävä
# kuhanPituus = float(input('Kirjoita Kuhan pituuden senttimetreinä: '))
#
# if kuhanPituus < 37:
#     print('Laske kuha takaisin järveen, sillä alimmasta sallitusta pyyntimitasta puuttuu ', 37 - kuhanPituus, 'cm')
# elif kuhanPituus >= 37:
#     print('Kuhan pituus on sopiva, ei tarvi olla nälkäinen tänään 😎')

# 2. tehtävä
# hyttiluokka = str(input('Valitse hyttiluokka (vaihtoehdot: LUX, A, B tai C): '))
#
# if hyttiluokka == 'LUX':
#     print('parvekkeellinen hytti yläkannella')
# elif hyttiluokka == 'A':
#     print('ikkunallinen hytti autokannen yläpuolella')
# elif hyttiluokka == 'B':
#     print('ikkunaton hytti autokannen yläpuolella')
# elif hyttiluokka == 'C':
#     print('ikkunaton hytti autokannen alapuolella')
# else:
#     print('Virheellinen hyttiluokka')

# 3. tehtävä
# sukupuoli = str(input('Valitse sukupuoli (mies vai nainen): '))
# hemo = float(input('Kirjoita hemoglobiini arvosi: '))
#
# if sukupuoli == 'nainen' and 117 <= hemo <= 175:
#     print('hemoglobiini arvosi ovat normaali tasolla')
# elif sukupuoli == 'nainen' and hemo < 117:
#     print('hemoglobiini arvosi ovat liian alhaiset')
# elif sukupuoli == 'nainen' and hemo > 175:
#     print('hemoglobiini arvosi ovat liian ylhäiset')
# elif sukupuoli == 'mies' and 134 <= hemo <= 195:
#     print('hemoglobiini arvosi ovat normaali tasolla')
# elif sukupuoli == 'mies' and hemo < 134:
#     print('hemoglobiini arvosi ovat liian alhaiset')
# elif sukupuoli == 'mies' and hemo > 195:
#     print('hemoglobiini arvosi ovat liian ylhäiset')
# else: print('Pistit selvästi jotain väärin, tee uudelleen')

# 4. tehtävä
# vuosi = int(input('Kirjoita vuosiluku: '))
#
# print(vuosi)
#
# karkausvuosiCalc = vuosi / 4
# karkausvuosi = karkausvuosiCalc == int(karkausvuosiCalc)
#
# karkausvuosiCalc2 = vuosi / 400
# karkausvuosi2 = karkausvuosiCalc2 == int(karkausvuosiCalc2)
#
# if karkausvuosi:
#     print(vuosi, 'vuosi on karkausvuosi')
# else: print(vuosi, 'ei ole karkausvuosi')
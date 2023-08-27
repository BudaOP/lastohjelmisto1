# 1. tehtävä
# import random
#
# arpaL = []
# summa = 0
#
# arpa_input = int(input('Kirjoita arpakuutioiden lukumäärä: '))
#
# for luku in range(arpa_input):
#     arpaL.append(random.randint(1,6))
#
# for i in range(0,len(arpaL)):
#     summa = summa + arpaL[i]
#
# print('Arpakuutioiden luvut: ',arpaL)
# print(f'Arpakuutioiden määrä on {arpa_input} ja silmälukujen summa on {summa}')

# 2. tehtävä
# luvut = []
#
# luku = input('Anna luku tai lopeta painamalla ENTER: ')
#
# while luku!="":
#     luvut.append(luku)
#     luku = input('Anna luku tai lopeta painamalla ENTER: ')
# luvut.sort(reverse=True)
#
# print(luvut[0:5])

# 3. tehtävä
# luku = int(input('Kirjoita luku tarkistaakseen onko se alkuluku: '))
#
# # kaikki luvut, jotka eivät ole alkulukuja ovat jaollisia joko 2 tai 3. eli
# luku1 = luku / 2
# luku2 = luku / 3
#
# if luku1 == int(luku1) or luku2 == int(luku2):
#     print(f'{luku} ei ole alkuluku')
# else:
#     print(f'{luku} on alkuluku')
#
# # 4. tehtävä
# kaupungit = []
# kaupunki = ''
#
# for i in range(5):
#     kaupunki = input('Kirjoita kaupungin nimi: ')
#     kaupungit.append(kaupunki)
#
# for i in range(len(kaupungit)):
#     print(kaupungit[i])
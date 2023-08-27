# 5. tehtävä
leiviskät_str = input('Anna leiviskät: ')
naulat_str = input('Anna naulat: ')
luodit_str = input('Anna luodit: ')

leiviskät = float(leiviskät_str)
naulat = float(naulat_str)
luodit = float(luodit_str)

luotiCalc = (leiviskät * 20 + naulat) * 32 + luodit
massaCalc = (luotiCalc * 13.3) / 1000

kg = int(massaCalc)
g = round((massaCalc - int(massaCalc)) * 1000, 2)

print('Massa nykymittojen mukaan:\n', kg, 'kilogrammaa ja', g, 'grammaa')
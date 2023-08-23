# 1. tehtävä
userName = input('Kirjoita nimesi: ')
print('Hei, ' + userName + '!')

# 2. tehtävä
import math

säde_str = input('Kirjoita ympyrän säde (metri): ')
säde = int(säde_str)
ympyränA = säde**2 * math.pi
print('Ympyrän pinta-ala on ', round(ympyränA), 'metriä')

# 3. tehtävä
kanta = int(input("Anna suorakulmion kannan pituus : "))
korkeus = int(input("Anna suorakulmion korkeus : "))

piiri = kanta * 2 + korkeus * 2
pintaAla = kanta * korkeus

print('Suorakulmion piiri on ', piiri, 'ja pinta-ala on', pintaAla)

# 4. tehtävä
a = int(input('Kirjoita ensimmäinen luku: '))
b = int(input('Kirjoita toinen luku: '))
c = int(input('Kirjoita kolmas luku: '))

summa = a + b + c
tulo = a * b * c
keskiarvo = (a + b + c) / 3

print('Lukujen summa on', summa, '\nLukujen tulo on', tulo, '\nLukujen keskiarvo on', int(keskiarvo))

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

# 6. tehtävä
import random

# 3digit

a = str(random.randint(0, 9))
b = str(random.randint(0, 9))
c = str(random.randint(0, 9))


numerokoodi1 = a+b+c

print(f'3digit code: {numerokoodi1}')

# 4digit

d = str(random.randint(1, 6))
e = str(random.randint(1, 6))
f = str(random.randint(1, 6))
g = str(random.randint(1, 6))

numerokoodi2 = d+e+f+g
print(f'4digit code: {numerokoodi2}')


#toinen tapa 4digit
numerot = random.sample(range(1, 6), 4)

numerokoodi3 = str(numerot[0]) + str(numerot[1]) + str(numerot[2]) + str(numerot[3])

print(f'4digit code: {numerokoodi3}')


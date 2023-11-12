# 3. tehtävä
luku = int(input('Kirjoita luku tarkistaakseen onko se alkuluku: '))

# kaikki luvut, jotka eivät ole alkulukuja ovat jaollisia joko 2 tai 3. eli
luku1 = luku / 2
luku2 = luku / 3

if luku1 == int(luku1) or luku2 == int(luku2):
    print(f'{luku} ei ole alkuluku')
else:
    print(f'{luku} on alkuluku')
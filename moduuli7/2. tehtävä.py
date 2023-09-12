uusnimi = input('Kirjoita joku nimi: ')
nimilista = set()
nimilista.add(uusnimi)

while uusnimi != '':
    uusnimi = input('Kirjoita joku nimi: ')
    if uusnimi in nimilista:
        print('Aiemmin syötetty nimi')
    else:
        nimilista.add(uusnimi)
        print('Uusi nimi')
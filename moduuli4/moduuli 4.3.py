# 3. tehtävä
luku = input('Kirjoita luku: ')

if luku != '':
    max = int(luku)
    min = int(luku)

    while luku != '':
        luku1 = int(luku)

        if luku1 > max:
            max = luku1

        if luku1 < min:
            min = luku1

        luku = input('Kirjoita seuraava luku: ')
    print('Suurin arvo:', max)
    print('Pienin arvo:', min)
syöttö = input('1. uusi lentoasema 2. lentoaseman haku 3. lopeta toiminto\nValitse toiminto: ')

lentoasemat = {}

while syöttö != 'lopeta toiminto':
    if syöttö == 'uusi lentoasema':
        icao = input('Kirjoita ICAO-koodi: ')
        nimi = input('Kirjoita lentoaseman nimi: ')
        print(f'\n---\nLentoasema {nimi} lisätty rekisteriin\n---\n')
        lentoasemat[icao] = nimi
    if syöttö == 'lentoaseman haku':
        icao = input('Kirjoita ICAO-koodi: ')
        if icao in lentoasemat:
            print(f'\n---\nLentoaseman nimi on {lentoasemat[icao]}\n---\n')
        else:
            print('\n---\nSellaista lentoasemaa ei löytynyt\n---\n')
    syöttö = input('1. uusi lentoasema 2. lentoaseman haku 3. lopeta toiminto\nValitse toiminto: ')


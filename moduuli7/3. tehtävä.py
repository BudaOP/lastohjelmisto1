syotto = input('1. lisäys 2. haku 3. lopeta 4. katso lista 5. poista\nValitse toiminto: ')

lentoasemat = {}

while syotto != 'lopeta':
    if syotto == 'lisäys':
        icao = input('Kirjoita ICAO-koodi: ')
        nimi = input('Kirjoita lentoaseman nimi: ')
        kyllaei = input(f'...\nHaluatko varmasti lisätä lentoaseman {icao.upper()} : {nimi} rekisteriin?\n'
                        f'Vahvista painamalla Enter tai palaa takaisin painamalla e: ')
        if kyllaei == '':
            print(f'\n---\nLentoasema {nimi} lisätty rekisteriin\n---\n')
            lentoasemat[icao] = nimi
        elif kyllaei == 'e':
            print('\nLentoaseman lisääminen peruuttiin\n')
        else:
            print('\nOdottamaton syöte, toiminto peruutetaan...\n')
    if syotto == 'haku':
        icao = input('Kirjoita ICAO-koodi: ')
        if icao in lentoasemat:
            print(f'\n---\nLentoasemasi on {lentoasemat[icao]}\n---\n')
        else:
            print('\n---\nSellaista lentoasemaa ei löytynyt\n---\n')
    if syotto == 'katso lista':
        print(lentoasemat)
    u = 0
    if syotto == 'poista':
        print('\nLentoasemien lista:')
        for i in lentoasemat:
            u += 1
            print(f'{u}. {i} : {lentoasemat[i]}')
        poista = input('\nAnna ICAO-koodi poistaakseen lentoaseman: ')
        if poista in lentoasemat:
            kyllaei = input(f'Oletko varma, että haluat poistaa {lentoasemat[poista]} lentoaseman?\n'
                            f'Vahvista painamalla Enter tai palaa takaisin painamalla e:')
            if kyllaei == '':
                print(f'\nLentoasema {lentoasemat[poista]} on onnistuneesti poistettu rekisteristä\n')
                lentoasemat.pop(poista)
            elif kyllaei == 'e':
                print('\nLentoaseman poistaminen peruutettiin\n')
            else:
                print('\nOdottamaton syöte, toiminto peruutetaan...\n')
        else:
            print('\nOdottamaton syöte, toiminto peruutetaan...\n')
    syotto = input('1. lisäys 2. haku 3. lopeta 4. katso lista 5. poista\nValitse toiminto: ')
print('...\nOhjelma sammuu')


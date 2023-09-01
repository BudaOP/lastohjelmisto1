def gallo(b):
    while b >= 0:
        litrat = b * l
        print(litrat)
        b = float(input('Kirjoita gallonamäärän: '))
    else:
        print('Syötit negatiivisen luvun')

l = 3.785
b = float(input('Kirjoita gallonamäärän: '))
gallo(b)
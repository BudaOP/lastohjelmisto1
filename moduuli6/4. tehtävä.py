def list_calc(lista):
    summa = 0
    for i in lista:
        summa = summa + i
    # print(summa)
    return summa

my_list = [3, 5, 76, 7, 5]
print('Listan lukujen summa on:', list_calc(my_list))


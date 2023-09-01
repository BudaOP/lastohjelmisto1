def karsittulista(lista):
    karsittu_lista = []
    for i in lista:
        if i % 2 == 0:
            karsittu_lista.append(i)
    return karsittu_lista

lista = [3,5,8,4,12,13]
print(f'Alkuperäinen lista: {lista}\nParilliset luvut listalta: {karsittulista(lista)}')
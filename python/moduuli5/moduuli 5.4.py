# 4. tehtävä
kaupungit = []
kaupunki = ''

for i in range(5):
    kaupunki = input('Kirjoita kaupungin nimi: ')
    kaupungit.append(kaupunki)

for i in range(len(kaupungit)):
    print(kaupungit[i])
# 2. tehtävä
luvut = []

luku = input('Anna luku tai lopeta painamalla ENTER: ')

while luku!="":
    luvut.append(luku)
    luku = input('Anna luku tai lopeta painamalla ENTER: ')
luvut.sort(reverse=True)

print(luvut[0:5])
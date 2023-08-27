# 1. tehtävä
luku = 0

while luku < 1000:
    luku = luku + 1
    lukuCalc = luku / 3
    tulos = lukuCalc == int(lukuCalc)
    if tulos:
        print(luku)
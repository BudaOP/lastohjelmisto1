# 3. tehtävä
sukupuoli = str(input('Valitse sukupuoli (mies vai nainen): '))
hemo = float(input('Kirjoita hemoglobiini arvosi: '))

if sukupuoli == 'nainen' and 117 <= hemo <= 175:
    print('hemoglobiini arvosi ovat normaali tasolla')
elif sukupuoli == 'nainen' and hemo < 117:
    print('hemoglobiini arvosi ovat liian alhaiset')
elif sukupuoli == 'nainen' and hemo > 175:
    print('hemoglobiini arvosi ovat liian ylhäiset')
elif sukupuoli == 'mies' and 134 <= hemo <= 195:
    print('hemoglobiini arvosi ovat normaali tasolla')
elif sukupuoli == 'mies' and hemo < 134:
    print('hemoglobiini arvosi ovat liian alhaiset')
elif sukupuoli == 'mies' and hemo > 195:
    print('hemoglobiini arvosi ovat liian ylhäiset')
else: print('Pistit selvästi jotain väärin, tee uudelleen')
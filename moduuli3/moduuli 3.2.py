# 2. tehtävä
hyttiluokka = str(input('Valitse hyttiluokka (vaihtoehdot: LUX, A, B tai C): '))

if hyttiluokka == 'LUX':
    print('parvekkeellinen hytti yläkannella')
elif hyttiluokka == 'A':
    print('ikkunallinen hytti autokannen yläpuolella')
elif hyttiluokka == 'B':
    print('ikkunaton hytti autokannen yläpuolella')
elif hyttiluokka == 'C':
    print('ikkunaton hytti autokannen alapuolella')
else:
    print('Virheellinen hyttiluokka')
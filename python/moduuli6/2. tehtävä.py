import random, time

# Tein koodin joka heittää joka sekunti uudelleen noppaa niin kauan
# ,kunnes se saa luvuksi kyseisen nopan suurin luku

def randomluku(x):
    n = random.randint(1,x)
    print(f'{p}. nopan heiton luku on {n}')
    time.sleep(1)
    return n

i = 0
p = 0

x = int(input('Kirjoita nopan tahkojen yhteismäärä: '))

while i != x:
    p = p + 1
    i = randomluku(x)
    if i == x:
        print(f'noppaa heitettiin {p} kertaa, ennen kuin nopan suurin arvo saatiin. \nohjelma sammuu')
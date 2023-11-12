import random, time

# Koodi joka heittää noppaa niin kauan kunnes se saa luvuksi 6

print('Aloitetaan nopan heitto')

def randomluku():
    n = random.randint(1,6)
    print(f'{p}. nopan heiton luku on {n}')
    time.sleep(1)
    return n

i = 0
p = 0

while i != 6:
    p = p + 1
    i = randomluku()
    if i == 6:
        print('sammuu')
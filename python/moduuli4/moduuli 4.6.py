# 6. tehtävä
import random

N = int(input('Anna pisteiden kokonaismäärä: '))

n = 0

for i in range(N):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x ** 2 + y ** 2 <= 1:
        n += 1

pii = 4 * n / N
print(f'Piin likiarvo on {pii}')
# 4. tehtävä
import random

lukuX = random.randint(1,10)
lukuInput = int(input('Arvaa luku: '))

while lukuInput != lukuX:
    if lukuInput > lukuX:
        print('Liian suuri arvaus')
    elif lukuInput < lukuX:
        print('Liian pieni arvaus')
    lukuInput = int(input('Arvaa luku uudestaan: '))
print('Oikein')
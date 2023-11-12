# 6. tehtävä
import random

# 3digit

a = str(random.randint(0, 9))
b = str(random.randint(0, 9))
c = str(random.randint(0, 9))


numerokoodi1 = a+b+c

print(f'3digit code: {numerokoodi1}')

# 4digit

d = str(random.randint(1, 6))
e = str(random.randint(1, 6))
f = str(random.randint(1, 6))
g = str(random.randint(1, 6))

numerokoodi2 = d+e+f+g
print(f'4digit code: {numerokoodi2}')


#toinen tapa 4digit
numerot = random.sample(range(1, 6), 4)

numerokoodi3 = str(numerot[0]) + str(numerot[1]) + str(numerot[2]) + str(numerot[3])

print(f'4digit code: {numerokoodi3}')
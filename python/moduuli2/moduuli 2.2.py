# 2. tehtävä
import math

säde_str = input('Kirjoita ympyrän säde (metri): ')
säde = int(säde_str)
ympyränA = säde**2 * math.pi
print('Ympyrän pinta-ala on ', round(ympyränA), 'metriä')

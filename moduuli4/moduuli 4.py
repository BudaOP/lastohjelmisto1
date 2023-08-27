# # 1. tehtävä
# luku = 0
#
# while luku < 1000:
#     luku = luku + 1
#     lukuCalc = luku / 3
#     tulos = lukuCalc == int(lukuCalc)
#     if tulos:
#         print(luku)

# 2. tehtävä
# tuuma = float(input('Montako tuumaa: '))
#
# while tuuma >= 0:
#     print(f'{tuuma * 2.54} cm')
#     break

# 3. tehtävä
# luku = input('Kirjoita luku: ')
#
# if luku != '':
#     max = int(luku)
#     min = int(luku)
#
#     while luku != '':
#         luku1 = int(luku)
#
#         if luku1 > max:
#             max = luku1
#
#         if luku1 < min:
#             min = luku1
#
#         luku = input('Kirjoita seuraava luku: ')
#     print('Suurin arvo:', max)
#     print('Pienin arvo:', min)

# 4. tehtävä
# lukuX = random.randint(1,10)
# lukuInput = int(input('Arvaa luku: '))
#
# while lukuInput != lukuX:
#     if lukuInput > lukuX:
#         print('Liian suuri arvaus')
#     elif lukuInput < lukuX:
#         print('Liian pieni arvaus')
#     lukuInput = int(input('Arvaa luku uudestaan: '))
# print('Oikein')

# 5. tehtävä
# user_input = input('Kirjoita käyttäjätunnus: ')
# password_input = input('Kirjoita salasanasi: ')
#
# username = 'python'
# password = 'rules'
# väärin = 0
#
# if user_input == username and password_input == password:
#     print('oikein')
#
#
# while True:
#     if user_input != username or password_input != password:
#         väärin += 1
#         print(f'Käyttäjätunnus tai salasana on väärin. Kokeile uudelleen. Yrityksiä jäljellä {5 - väärin + 1}.')
#         user_input = input('Kirjoita käyttäjätunnus: ')
#         password_input = input('Kirjoita salasanasi: ')
#         if user_input == username and password_input == password:
#             print('Oikein')
#             break
#         if väärin == 5:
#             print('Pääsy evätty')
#             break

# 6. tehtävä
# liian vaikee tehtävä tai liian huonosti selitettynä
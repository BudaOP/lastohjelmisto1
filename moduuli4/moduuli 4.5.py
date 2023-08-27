# 5. tehtävä
user_input = input('Kirjoita käyttäjätunnus: ')
password_input = input('Kirjoita salasanasi: ')

username = 'python'
password = 'rules'
väärin = 0

if user_input == username and password_input == password:
    print('oikein')


while True:
    if user_input != username or password_input != password:
        väärin += 1
        print(f'Käyttäjätunnus tai salasana on väärin. Kokeile uudelleen. Yrityksiä jäljellä {5 - väärin + 1}.')
        user_input = input('Kirjoita käyttäjätunnus: ')
        password_input = input('Kirjoita salasanasi: ')
        if user_input == username and password_input == password:
            print('Oikein')
            break
        if väärin == 5:
            print('Pääsy evätty')
            break
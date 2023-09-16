import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='KierukkaKupariNöö7!',
         autocommit=True
         )

def haelenttis(icao):
    sql = f"SELECT name, municipality FROM airport WHERE airport.ident = '{icao}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

icao = input('Kirjoita ICAO -koodi: ')
print(*haelenttis(icao))

# Siistimpi tapa tulostaa
if haelenttis(icao):
    name, municipality = haelenttis(icao)[0]
    tulos = f"Lentokenttä on {name} ja sen sijaintikunta on {municipality}"
    print(tulos)
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='KierukkaKupariNöö7!',
         autocommit=True
         )

def lenttislista(maakoodi):
    sql = f"SELECT type, COUNT(*) AS lukumäärä FROM airport WHERE iso_country = '{maakoodi}' GROUP BY type;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

# ylimääräinen, tehty sitä varten, että saan paremman tuloksen
def maahaku(maakoodi):
    sql = f"SELECT DISTINCT country.name FROM country, airport WHERE airport.iso_country = country.iso_country AND country.iso_country = '{maakoodi}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


maakoodi = input('Kirjoita haluamasi maakoodi: ')
lenttistype = lenttislista(maakoodi)
maa = maahaku(maakoodi)

# tylsä tapa tulostaa
print(*lenttistype)

# toinen tapa
if maa:
    maailman = maa[0][0]
    print(f"\nHere's list of airports in {maailman}:")
for tyyppi, count in lenttistype:
    tyyppi = tyyppi.replace("_", " ").capitalize()
    print(f"TYPE: {tyyppi:<15} AMOUNT: {count}")


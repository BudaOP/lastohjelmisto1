import mysql.connector, geopy.distance, time

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='KierukkaKupariNöö7!',
         autocommit=True
         )

def lenttiscoords(icao1,icao2):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident IN ('{icao1}','{icao2}');"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    sql2 = (f"SELECT airport.name FROM country, airport WHERE airport.iso_country = country.iso_country "
            f"AND airport.ident IN ('{icao1}','{icao2}') ORDER BY FIELD(airport.ident,'{icao1}','{icao2}')")
    kursori.execute(sql2)
    lenttistulos = kursori.fetchall()
    return tulos, lenttistulos

icao1 = input('Write first ICAO code: ')
icao2 = input('Write second ICAO code: ')

koordinaatit, lenttis = lenttiscoords(icao1, icao2)

if koordinaatit and lenttis:
    koord1, koord2 = koordinaatit
    lenttis1, lenttis2 = lenttis
    valimatka = geopy.distance.distance(koord1, koord2).km
    print(f"\n{lenttis1[0]} coordinates are {koord1} and {lenttis2[0]} coordinates are {koord2}\n")
    print(f"Calculating, wait for a moment...\n")
    time.sleep(2)
    print(f"Distance between {lenttis1[0]} and {lenttis2[0]} is {valimatka:.0f} km")
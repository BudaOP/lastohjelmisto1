import mysql.connector
from flask import Flask

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='KierukkaKupariNöö7!',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def lentokentta(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    name, municipality = tulos[0]

    lenttis = {
        "ICAO": icao.upper(),
        "Name": name,
        "Municipality": municipality,
    }

    return lenttis

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
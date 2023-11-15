from flask import Flask

app = Flask(__name__)
@app.route('/isprime/<luku1>')
def isPrime(luku1):
    luku = int(luku1)

    if luku % 2 == 0 or luku % 3 == 0:
        vastaus = {
            "Luku": luku,
            "isPrime": 'false',
        }
    else:
        vastaus = {
            "Luku": luku,
            "isPrime": 'true',
        }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
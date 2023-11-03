import requests

pyyntö = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(pyyntö).json()
value = vastaus['value']

print(f"\nTässä on päivän Chuck Norris vitsi:\n{value}")

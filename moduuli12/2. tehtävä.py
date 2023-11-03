import requests


city = input('Kirjoita kaupunkisi: ').capitalize()

api_key = "3de078a754c73ba031e3fef445b861e3"
limit = 1

url_geo = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={api_key}"

response_geo = requests.get(url_geo).json()

if response_geo:
    latitude = response_geo[0]['lat']
    longitude = response_geo[0]['lon']
    url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response_weather = requests.get(url_weather).json()

    if 'weather' in response_weather and 'main' in response_weather:
        weather_description = response_weather['weather'][0]['description']
        temperature_kelvin = response_weather['main']['temp']

        temperature_celsius = temperature_kelvin - 273.15

        print(f"City: {city}")
        print(f"Weather: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
    else:
        print(f"Could not retrieve weather information for {city}")
else:
    print(f"Location information for {city} not found.")

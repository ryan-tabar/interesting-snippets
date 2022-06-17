import requests
import json

api_key = "5d5c88002278a4fbef29d7752e855e0e"
#London
lat = 51.5072
lon = 0.1276
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
response = requests.get(url)

ok = 200
if response.status_code == ok:
    data = response.json()
    with open("weather.txt", "w") as file:
        file.write(json.dumps(data, indent=2))
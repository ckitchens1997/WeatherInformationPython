import requests
from pprint import pprint

API_KEY = 'dd0c0e8a7d0ce8e463172b3c97154c1e'

city = input('Enter a city: ')

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_KEY+'&q='+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
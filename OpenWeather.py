# Evan
# ekirchst@uci.edu
# 59946460
from urllib import request
import json as js
from datetime import datetime


class OpenWeather:
    '''
    Weather API Class Created to Interact with OpenWeather api
    '''
    def __init__(self, zipcode, ccode):
        '''
        Initializes OpenWeather Object
        Takes in zipcode and ccode
        '''
        self.zip_code = zipcode
        self.country_code = ccode
        self.url = 'https://api.openweathermap.org/data/2.5'

    def set_apikey(self, apikey:str) -> None:
        self.apikey = apikey

    
    def load_data(self) -> None:
        temp = f"{self.url}/weather?zip={self.zip_code},{self.country_code}&appid={self.apikey}"
        response = request.urlopen(temp)
        re = js.loads(response.read())
        self.temperature = re['main']['temp']
        self.high_temperature = re['main']['temp_max']
        self.low_temperature = re['main']['temp_min']
        self.longitude = re['coord']['lon']
        self.latitude = re['coord']['lat']
        self.description = re['weather'][0]['description']
        self.humidity = re['main']['humidity']
        self.sunset = datetime.utcfromtimestamp(re['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
        self.city = re['name']
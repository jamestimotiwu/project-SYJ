#
# Add feature to suggest clothing to wear etc.
# Add icons to associate weather
# Improve graphics
#
#
# Author: James Timotiwu
# Weather Module
#

import json
from urllib2 import urlopen

#
#
class Weather():

    global data

    # Generate a full url to JSON request
    # returns json url 
    def get_url(self):
        user_api = '26bbb2c6a8df816a7a67d2d82f29136e'  # Obtain yours form: http://openweathermap.org/
        unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
        api = 'http://api.openweathermap.org/data/2.5/weather?id=4833320'     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

        full_api_url = api + '&mode=json&units=' + unit + '&APPID=' + user_api
        return full_api_url

    # Converts url to parsable JSON dictionary
    # returns raw JSON dictionary
    def load_weather_data(self, full_api_url):
        url = urlopen(full_api_url)
        raw_api_dict = json.loads(url.read().decode('utf-8'))
        url.close()
        return raw_api_dict

    def weather_data(self):

        return self.get_weather_data(self.load_weather_data(self.get_url()))

    # Collects and organizes dictionary into appropriate variables
    # returns python dictionary structure
    def get_weather_data(self, raw_api_dict):
        
        data = dict(
            city=raw_api_dict.get('name'),
            country=raw_api_dict.get('sys').get('country'),
            temp=raw_api_dict.get('main').get('temp'),
            temp_max=raw_api_dict.get('main').get('temp_max'),
            temp_min=raw_api_dict.get('main').get('temp_min'),
            humidity=raw_api_dict.get('main').get('humidity'),
            pressure=raw_api_dict.get('main').get('pressure'),
            sky=raw_api_dict['weather'][0]['main'],
            wind=raw_api_dict.get('wind').get('speed'),
            getwindspeed_deg=raw_api_dict.get('deg'),
            cloudiness=raw_api_dict.get('clouds').get('all')
        )
        return data
    
    #
    #
    #
#    def get_recommend_outfit(self):
        #
        #
        #
        #
        #
        #

    # Updates current temperature data
    # returns temperature
    def update_temp(self):

        raw_data = self.load_weather_data(self.get_url())
        return raw_data.get('main').get('temp')

    #Returns city, country data
    def getloc(self):
        return self.data['city'], data['country']

    #
    #
    def maxmintemp(self):
        return self.data['temp_max'], data['temp_min']
    
    #
    #
    def update_windspeed(self):
        raw_data = load_weather_data(self.get_url())
        return raw_data.get('wind').get('speed')
    
    #
    #
    def gethumidity(self):
        return self.data['humidity']
    
    #
    #
    def getpressure(self):
     
        return self.data['pressure']

    def __init__(self, **kwargs):
        m_symbol = 'C'
        data = self.weather_data() 
#        locationdes='Current weather in: {}, {}'.format(data['city'], data['country'])
#        temp='{}{}, {}'.format(data['temp'], m_symbol, data['sky'])
#        maxmin='Max: {}, Min: {}'.format(data['temp_max'], data['temp_min'])
#        windspeed='Wind Speed: {} mph'.format(data['wind'])
#        clouds='Clouds: {}'.format(data['cloudiness'])
#        humidity='Humidity: {}'.format(data['humidity'])
#        pressure='Pressure: {}'.format(data['pressure'])
#
    def update(self, event):
        self.btn.text = user.getUser()


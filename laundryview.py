#
# Author: James Timotiwu
# LaundryView Module
#

import json
from urllib2 import urlopen

class LaundryView():

    def get_url(self):
        user_api = '26bbb2c6a8df816a7a67d2d82f29136e'  # Obtain yours form: http://openweathermap.org/
        api = 'http://api.openweathermap.org/data/2.5/weather?id=4833320'     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

        full_api_url = api + '&mode=json&units=' + unit + '&APPID=' + user_api
        return full_api_url

    def load_laundryview(self, full_api_url):
        
        url = urlopen(full_api_url)
        raw_api_dict = json.loads(url.read().decode('utf-8'))
        url.close()
        return raw_api_dict

    def get_laundry_stat(self, raw_api_dict):

    def get_laundry_label(self, machineid):

    def update_laundry_status(self, machineid):

    def update_laundry_eta(self, machineid):



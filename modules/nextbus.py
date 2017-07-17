#
# Author: James Timotiwu
# NextBus Module 
#

import json
from urllib2 import urlopen

class NextBus():
    #
    # Commands:
    # routeList
    # routeConfig
    # predictions
    # predictionsForMultistops
    # schedule
    # messages
    # vehicleLocations
    #
    def get_url(self, command, route_tag, stop_tag):
        agency_tag = 'case-western'  # Obtain yours form: http://openweathermap.org/
        full_api_url = 'http://webservices.nextbus.com/service/publicJSONFeed?command='
        + command + '&a=' + agency_tag # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

  
        return full_api_url

    def load_nextbus(self, full_api_url):
        
        url = urlopen(full_api_url)
        raw_api_dict = json.loads(url.read().decode('utf-8'))
        url.close()
        return raw_api_dict

    def get_nextbus_stat(self, raw_api_dict):



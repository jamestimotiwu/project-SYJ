#
# Author: James Timotiwu
# KUI
#

import modules.weather as wtr
import json
import kivy
from kivy.uix import layout

kivy.require('1.8.0') # replace with your current kivy version !

from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.graphics.svg import Svg

from kivy.config import Config
from kivy.properties import ObjectProperty,ListProperty,NumericProperty,StringProperty #importing kivy properties
from kivy.network.urlrequest import UrlRequest
from kivy.uix.listview import ListItemButton
from urllib2 import urlopen

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '320')

class Container(AnchorLayout):
   
    def __init__(self, **kwargs):
        m_symbol = 'C'
        data = wtr.Weather().weather_data()  
        super(Container, self).__init__(**kwargs)
        locationdes='{}, {}'.format(data['city'], data['country'])
        temp='{}{}, {}'.format(data['temp'], m_symbol, data['sky'])
        maxmin='Max: {}, Min: {}'.format(data['temp_max'], data['temp_min'])
        windspeed='Wind Speed: {} mph'.format(data['wind'])
        clouds='Clouds: {}'.format(data['cloudiness'])
        humidity='Humidity: {}'.format(data['humidity'])
        pressure='Pressure: {}'.format(data['pressure'])

        img1 = AsyncImage(source="img/30.png", size_hint=(0.5, 0.5),
                pos_hint={'left':0.7})

#        img1 = Svg("img/40.svg")
        anchor_rt = AnchorLayout(anchor_x='left', anchor_y='top')
        lbl1 = Label(text=locationdes, size=(600, 120), size_hint=(None, None))
        lbl2 = Label(text=temp, size=(600, 155), size_hint=(None, None))
        lbl3 = Label(text=maxmin, size=(600, 190), size_hint=(None, None))
        lbl4 = Label(text=windspeed, size=(600,225), size_hint=(None, None))
        lbl5 = Label(text=clouds, size=(600, 255), size_hint=(None, None))
        lbl6 = Label(text=humidity, size=(600, 285), size_hint=(None, None))
        lbl7 = Label(text=pressure, size=(600, 330), size_hint=(None, None))
        anchor_rt.add_widget(lbl1)
        anchor_rt.add_widget(lbl2)
        anchor_rt.add_widget(lbl3)
        anchor_rt.add_widget(lbl4)
        anchor_rt.add_widget(lbl5)
        anchor_rt.add_widget(lbl6)
        anchor_rt.add_widget(lbl7)
        anchor_rt.add_widget(img1)
        self.add_widget(anchor_rt)

        #anchor_rb = AnchorLayout(anchor_x='right', anchor_y='bottom')
        #rbb = Button(text="Test", size=(265, 140), size_hint=(None, None))
        #anchor_rb.add_widget(rbb)
        #self.add_widget(anchor_rb)

    def update(self, event):
        self.btn.text = user.getUser()

class MyJB(App):
    def build(self):

        parent = Container()

        return parent

if __name__ == '__main__':
    MyJB().run()

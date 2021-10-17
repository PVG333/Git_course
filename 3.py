#import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
#owm = pyowm.OWM('93c4ed227d4d86a037d1a7092188d7df')

#place = input ("В каком городе/стране?: ")

#observation = owm.weather_at_place(place)
#w = observation.get_weather()

#print(w)

owm = OWM('93c4ed227d4d86a037d1a7092188d7df')
mgr = owm.weather_manager()

place = input ("В каком городе/стране?: ")
observation = mgr.weather_at_place(place)
w = observation.weather
print(w)


print("Hello Git")
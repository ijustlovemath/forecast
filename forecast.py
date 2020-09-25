#!/usr/bin/env python3
import sys
import webbrowser

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="ijustlovemath forecast app")

location = lambda:0
location.latitude = 0.0
location.longitude = 0.0

name = ' '.join(arg for arg in sys.argv[1:])
location = geolocator.geocode(name)
if location is None:
    print("please provide a location in the arguments")
    quit()

url_base = "https://forecast.weather.gov/MapClick.php?lat={:.4f}&lon={:.4f}&unit=0&lg=english&FcstType=graphical"
url = url_base.format(location.latitude, location.longitude)

print("Forecast is here: " + url)
webbrowser.open(url)

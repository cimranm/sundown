#! /usr/bin/env python3

from datetime import date
from suntime import Sun, SunTimeException


import location 
from  geopy.geocoders import Nominatim



geolocator = Nominatim(user_agent="http")

country     = "Australia"
city        = "Sydney"



loc = geolocator.geocode (f'{city},{country}')

lat  = loc.latitude
long = loc.longitude

# Suntime

sun = Sun(lat, long)

date = date.today()



risetime    = sun.get_local_sunrise_time(date)
settime     = sun.get_local_sunset_time(date)

print (f"RISE: {risetime.strftime('%H:%M')}")

print (f"SET: {settime.strftime('%H:%M')}")
#settime     = sun.get_sunset










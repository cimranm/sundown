#! /usr/bin/env python3

# location.py

from  geopy.geocoders import Nominatim

def get_location():

    geolocator = Nominatim(user_agent="http")

    country     = "Australia"
    city        = "Sydney"

    loc = geolocator.geocode (f'{city},{country}')
    return (loc.latitude, loc.longitude)

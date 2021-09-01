#! /usr/bin/env python3

from datetime import date
from suntime import Sun, SunTimeException

import location 

def get_sun():

    lat, long = location.get_location()

    # Suntime
    sun = Sun(lat, long)
    return sun

def rise_print():
    # SUNRISE
    date = get_date()
    sun = get_sun()
    time = sun.get_local_sunrise_time(date)

    print (f"RISE: {time.strftime('%H:%M')}")

def set_print():
    # SUNSET
    date = get_date()
    sun = get_sun()
    time = sun.get_local_sunset_time(date)

    print (f"SET: {time.strftime('%H:%M')}")

def get_date():
    
    # TODO allow for specific dates
    return date.today()






# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:02:42 2021
@author: james
"""

from FlightRadar24.api import FlightRadar24API
import math
fr_api = FlightRadar24API()

#Set redii to be chcked and checks through the different radii
def main(GPS_lat,GPS_lon,):
  #GPS_X is longitude 
  #GPS_Y is Lattitude
  #GPS_lon = -79.612208 #Pearson Airport
  #GPS_lat = 43.686540 #Pearson Airport
  #GPS_lon = -79.376102 #Lake Simcoe
  #GPS_lat = 44.434362 #Lake Simcoe
  #Radius to check in Kilometers
  radii = [1,10,25,50]
  result = 'Flights in the air:<br>'
  for radius in radii:
    result = result + "Within " + str(radius) + "km: " + str(check_flights(GPS_lon,GPS_lat,radius)) + "<br>"
  return result

#Checks flight flights with radius of the GPS
#https://calgary.rasc.ca/latlong.htm
def check_flights(GPS_lon,GPS_lat,radius):
  #Assuming flat ground and not on ellipsoid
  #1 degree of lattitude in KM at current GPS
  lat_scale =  111.13295 - 0.55982 * math.cos(math.radians(2 * GPS_lon)) + 0.00117 * math.cos(math.radians(4 * GPS_lon))
  #1 degree of lon in KM at current GPS
  lon_scale = 111.41288 * math.cos(math.radians(GPS_lat)) - 0.09350 * math.cos(math.radians(3 * GPS_lat)) + 0.00012 * math.cos(math.radians(5 * GPS_lat))
  lat_change = radius/lat_scale
  lon_change =  radius/lon_scale
  #Create Bounding Box
  #'tly,bry,tlx,brx'
  bounds = str(GPS_lat+lat_change) + "," + str(GPS_lat-lat_change) + "," + str(GPS_lon-lon_change) + "," + str(GPS_lon+lon_change)
  #Search for Flights
  flights = fr_api.get_flights(bounds = bounds)
  #Filter out flights on ground
  flights_in_air = 0
  for flight in flights:
    if not flight.__dict__['on_ground']:
      flights_in_air = flights_in_air + 1

  #Return number of flights
  return flights_in_air
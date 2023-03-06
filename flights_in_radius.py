# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:02:42 2021
@author: james
"""

from FlightRadar24.api import FlightRadar24API
import math
fr_api = FlightRadar24API()

def calculate_distance(x1,y1,x2,y2,x_scale=1,y_scale=1):
  # Point 1 should be the centre
  x_distance = (x2 - x1)*x_scale # in km
  y_distance = (y2 - y1)*y_scale # in km
  total_distance = ((x_distance)**2 + (y_distance)**2)**0.5 # in km
  return (total_distance,x_distance,y_distance)


#Set redii to be chcked and checks through the different radii
def main(GPS_lat,GPS_lon,):
  #GPS_X is longitude 
  #GPS_Y is Lattitude
  #GPS_lon = -79.612208 #Pearson Airport
  #GPS_lat = 43.686540 #Pearson Airport
  #GPS_lon = -79.376102 #Lake Simcoe
  #GPS_lat = 44.434362 #Lake Simcoe
  #Radius to check in Kilometers
  radius = 25

  return (check_flights(GPS_lon,GPS_lat,radius))

#Checks flight flights with radius of the GPS
#https://calgary.rasc.ca/latlong.htm
def check_flights(GPS_lon,GPS_lat,max_radius):
  #Assuming flat ground and not on ellipsoid
  #1 degree of lattitude in KM at current GPS
  lat_scale =  111.13295 - 0.55982 * math.cos(math.radians(2 * GPS_lon)) + 0.00117 * math.cos(math.radians(4 * GPS_lon))
  #1 degree of lon in KM at current GPS
  lon_scale = 111.41288 * math.cos(math.radians(GPS_lat)) - 0.09350 * math.cos(math.radians(3 * GPS_lat)) + 0.00012 * math.cos(math.radians(5 * GPS_lat))
  lat_change = max_radius/lat_scale
  lon_change =  max_radius/lon_scale
  #Create Bounding Box
  #'tly,bry,tlx,brx'
  bounds = str(GPS_lat+lat_change) + "," + str(GPS_lat-lat_change) + "," + str(GPS_lon-lon_change) + "," + str(GPS_lon+lon_change)
  #Search for Flights
  flights = fr_api.get_flights(bounds = bounds)

  if max_radius < 10:
    max_radius = 10
  radii = [[1,0], 
           [int(max_radius*0.25),0], 
           [int(max_radius*0.5),0], 
           [int(max_radius*0.75),0], 
           [int(max_radius),0]]
  planes = []
  for flight in flights:
    #Filter out flights on ground
    if not flight.__dict__['on_ground']:
      distance = calculate_distance(GPS_lon,GPS_lat,flight.longitude,flight.latitude,lon_scale,lat_scale)
      for radius in radii:
        if distance[0] < radius[0]:
          radius[1] = radius[1] + 1
      planes.append((distance[1]/max_radius,distance[2]/max_radius,flight.heading))
      
  message = 'Flights in the air:<br>'
  for radius in radii:
    message = message + "Within " + str(radius[0]) + "km: " + str(radius[1]) + "<br>"
  #Return number of flights
  result = {
    "max-radius" : max_radius,
    "radii" : radii,
    "planes" : planes,
    "message" : message
  }
  return result


if __name__ == "__main__":
  #GPS_X is longitude 
  #GPS_Y is Lattitude
  #GPS_lon = -79.612208 #Pearson Airport
  #GPS_lat = 43.686540 #Pearson Airport
  #GPS_lon = -79.376102 #Lake Simcoe
  #GPS_lat = 44.434362 #Lake Simcoe
  #Radius to check in Kilometers
  GPS_lon,GPS_lat = (-79.6122,43.686540)
  # radii = [1,10,25]
  # result = 'Flights in the air:<br>'
  # for radius in radii:
    # result = result + "Within " + str(radius) + "km: " + str(check_flights(GPS_lon,GPS_lat,radius)) + "<br>"
  print(check_flights(GPS_lon,GPS_lat,25))
# flightVisualization.py
#
# Author:     Chi Nguyen
# Email:      nguyenct1@g.cofc.edu
# Class:      CITA 284 / CSCI 299   
# Assignment: Homework #5
# Due Date:   Mon, Mar 18, 2024
#
# Purpose:    Follows flight map data and create a visualization following
#             latitude, longitude, and altitude
#
# Input:   Flight data
#
# Output:  Visual representation

from image import *
from music import *
from gui import *
from string import *

# initialize displays and add airport labels
d = Display("Flight Visualization", 700, 550, 0, 0, Color.BLACK)
sgn = Label("Saigon", CENTER, Color.WHITE)
nrt = Label("Narita", CENTER, Color.WHITE)
d.add(sgn, 15, 525)
d.add(nrt, 620, 30)

img = "back.png"
d.drawImage(img, 0, 0)


# reading data
data = open("flightData.txt", "r")

# initializing data arrays
longitudeD = []
latitudeD  = []
altitudeD  = []

# reading data and appending each value to arrays
for line in data:
   time, longitude, latitude, altitude = split(line)
   longitude = float(longitude)
   latitude  = float(latitude)
   altitude  = int(altitude)
   latitudeD.append(latitude)          # reversed for y axis since
   latitudeDReversed = latitudeD[::-1] # it's flipped
   longitudeD.append(longitude)
   altitudeD.append(altitude)          # reversed for radius
   altitudeDReversed = altitudeD[::-1] # size gets larger based on alt
   
data.close()

# checking data arrays are appended correctly
print("longitude: " + str(longitudeD))
print("latitude: " + str(latitudeD))
print("altitude: " + str(altitudeD))

# setting ranges of data for mapping
longitudeMin   = min(longitudeD)
longitudeMax   = max(longitudeD)
latitudeMin    = min(latitudeDReversed)
latitudeMax    = max(latitudeDReversed)
altitudeMin    = min(altitudeD)
altitudeMax    = max(altitudeD)

for i in range(0, len(longitudeD), 3):
    longitude = longitudeD[i]
    latitude  = latitudeDReversed[i]
    altitude  = altitudeD[i]
    
    # mapping all data points
    xVal      = mapValue(longitude, longitudeMin, longitudeMax, 50, 650)
    yVal      = mapValue(latitude, latitudeMin, latitudeMax, 50, 500) + 10
    rad       = mapValue(altitude, altitudeMin, altitudeMax, 1, 25)
    greenVal  = mapValue(altitude, altitudeMin, altitudeMax, 1, 255)

    circle    = Circle(xVal, yVal, rad, Color(150, greenVal, 20)) 
    d.add(circle)

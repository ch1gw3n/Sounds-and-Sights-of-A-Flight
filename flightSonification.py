# flightSonification.py
#
# Author:     Chi Nguyen
# Email:      nguyenct1@g.cofc.edu
# Class:      CITA 284 / CSCI 299   
# Assignment: Homework #4
# Due Date:   Wed, Feb 28, 2024
#
# Purpose:    Follows flight map data and create a sonification following
#             latitude, longitude, and altitude
#
# Design:     
#     1. altitude  - highest register, soprano and mezzosoprano
#     2. latitude  - middle register, alto and tenor
#     3. longitude - lowest register, baritone and bass
#
# https://www.flightaware.com/live/flight/ANA834/history/20231230/0125ZZ/VVTS/RJAA

from music import *
from string import *

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
   longitudeD.append(longitude)
   latitudeD.append(latitude)
   altitudeD.append(altitude)
   
data.close()

# checking data arrays are appended correctly
print("longitude: " + str(longitudeD))
print("latitude: " + str(latitudeD))
print("altitude: " + str(altitudeD))

# building the score, phrases, and parts
flightScore    = Score("Flight Sonification", 90)

sopranoPart    = Part(CHOIR, 1)
mezzoPart      = Part(VOICE, 2)
altoPart       = Part(MUSIC_BOX, 3)
tenorPart      = Part(WARM_PAD, 4)
baritonePart   = Part(TAIKO, 5)
bassPart       = Part(ORGAN, 6)

sopranoPhrase  = Phrase()
mezzoPhrase    = Phrase()
altoPhrase     = Phrase()
tenorPhrase    = Phrase()
baritonePhrase = Phrase()
bassPhrase     = Phrase()

# setting ranges of data for mapping
longitudeMin   = min(longitudeD)
longitudeMax   = max(longitudeD)
latitudeMin    = min(latitudeD)
latitudeMax    = max(latitudeD)
altitudeMin    = min(altitudeD)
altitudeMax    = max(altitudeD)

# longitude as BASS
i = 0
while i < len(longitudeD):
   longPitch = mapScale(longitudeD[i], longitudeMin, longitudeMax, GF2, GF4, MINOR_SCALE)
   bass = Note(longPitch, HN, 60)        # lower registers as backing tracks, i didn't want  
   bassPhrase.addNote(bass)              # a lot of repitition so used half notes, iterating 
   i += 8                                # through every 8th data point so it ends together

# longitude as BARITONE
i = 4
while i < len(longitudeD):
   longPitch = mapScale(longitudeD[i], longitudeMin, longitudeMax, GF2, GF4, MINOR_SCALE)
   baritone = Note(longPitch, HN, 60)    # same logic as BASS, but starting at 4th data point
   baritonePhrase.addNote(baritone)      # so it uses points BASS is skipping
   i += 8

# latitude as TENOR
j = 0
while j < len(latitudeD):
   latPitch = mapScale(latitudeD[j], latitudeMin, latitudeMax, GF3, GF4, MINOR_SCALE)
   tenor = Note(latPitch, QN, 60)        # accompaniment so quarter note based, iterating
   tenorPhrase.addNote(tenor)            # through every 4th data point for timing
   j += 4
   
# latitude as ALTO
j = 2
while j < len(latitudeD):
   latPitch = mapScale(latitudeD[j], latitudeMin, latitudeMax, GF3, GF4, MINOR_SCALE)
   alto = Note(latPitch, QN, 60)         # same logic as TENOR, but starting at 2nd data
   altoPhrase.addNote(alto)              # point to fill in gaps
   Mod.retrograde(altoPhrase)            # reverse pitch direction bc it sounds cool
   j += 4                                # and represents the plane traveling further away

# altitude as MEZZOSOPRANO
k = 1
while k < len(altitudeD):
   altPitch = mapScale(altitudeD[k], altitudeMin, altitudeMax, GF3, GF5, MINOR_SCALE)
   mezzo = Note(altPitch, EN, 35)        # harmony, offset starting point to fill in gaps
   mezzoPhrase.addNote(mezzo) 
   #Mod.rotate(mezzoPhrase, 2)           # rotate and accent for funsies
   #Mod.accent(mezzoPhrase, 4, [3, 3], 1)
   k += 2

# altitude as SOPRANO
k = 0
while k < len(altitudeD):
   altPitch = mapScale(altitudeD[k], altitudeMin, altitudeMax, GF4, GF6, MINOR_SCALE)
   soprano = Note(altPitch, EN, 35)      # melody
   sopranoPhrase.addNote(soprano)
   #Mod.rotate(sopranoPhrase, 2)         # rotate and accent for funsies
   #Mod.accent(sopranoPhrase, 4, [1, 1], 1)
   k += 2

# adding all parts and phrases together
sopranoPart.addPhrase(sopranoPhrase)
mezzoPart.addPhrase(mezzoPhrase)
altoPart.addPhrase(altoPhrase)
tenorPart.addPhrase(tenorPhrase)
baritonePart.addPhrase(baritonePhrase)
bassPart.addPhrase(bassPhrase)

flightScore.addPart(sopranoPart)
flightScore.addPart(mezzoPart)
flightScore.addPart(altoPart)
flightScore.addPart(tenorPart)
flightScore.addPart(baritonePart)
flightScore.addPart(bassPart)

# the product
Write.midi(flightScore, "flightSonification.mid")
Play.midi(flightScore)
View.notate(flightScore)   
View.pianoRoll(flightScore)
#!/usr/bin/env python
# script  ./testdht-D6.py
# modifie boucle de capture
import grovepi, math, pymongo, time, pprint
from pymongo import MongoClient
from datetime import datetime
#
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
base_projetip = myclient["projetpi"]
# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 4  # The Sensor goes on digital port 4.
# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
#white = 1   # The White colored sensor.
print "----------------------"
print "Pour arreter faire Ctrl + C"
print "Debut : %s" % time.ctime()
# boucle de capture : on enregistre si valeur change
delaicaptures = 30  # en seconde
derniere_temperature = 0
derniere_humidite = 0
while True:
    try:
        # This example uses the blue colored sensor.
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(sensor,blue)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            ladate = datetime.now()
            c_date = ladate.strftime("%x") + " " + ladate.strftime("%X")
            c_temp = "%.02f"%(temp)
            c_humid = "%.02f%%"%(humidity)
#            print(" - " + c_date + "---" + c_temp + " --- " + c_humid + " - ")
            # envoi dans la base si valeurs changees
            if c_temp != derniere_temperature:
                base_projetip.captures.insert( { "date" : c_date, "source" : "hygrometrie", "unite" : "pourcent", "valeur" : c_humid } )
                print("temp  - " + c_date + "---" + c_temp)
                derniere_temperature = c_temp
            if c_humid != derniere_humidite:
                base_projetip.captures.insert( { "date" : c_date, "source" : "temperature", "unite" : "degre", "valeur" : c_temp } )
                print("humid  - " + c_date + "---" + c_humid)
                derniere_humidite = c_humid
	# attente en s
	time.sleep(delaicaptures)

    except IOError:
        print ("Error")

    except KeyboardInterrupt:
        print ("Arret utilisateur")
        break

#
print "Fin : %s" % time.ctime()
print "----------------------"


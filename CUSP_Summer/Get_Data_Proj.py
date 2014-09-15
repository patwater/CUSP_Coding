"""
add and save as Get_Data_Proj.py

import pyproj
proj = pyproj.Proj(init="esri:26918")
print proj(nyc_lon, nyc_lat)
"""

import sys
import urllib
import json
import collections
import pyproj
  
rawdata = urllib.urlopen("http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key="+sys.argv[1]+"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2])
busdata = json.load(rawdata)

print "Bus line: "+sys.argv[2]

# use the number of data objects in vehicle activity to count the number of active buses
print "Number of active buses: "+str(len(busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]))

# find and print every instance of lat and long
latitude =[]
longitude = []
proj = pyproj.Proj(init="esri:26918")

for i in range(len(busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])):
	latitude.append(busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"])
	longitude.append(busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"])

print "Location: Lat/Long"
for i in range(len(latitude)):
	print (latitude[i], longitude[i])


print "ESRI: 26918"
for i in range(len(latitude)):
	print proj(longitude[i], latitude[i])


"""
Your API key for the MTA Bus Time system is below.
08a616bb-c868-4f76-81fa-de1ca0da9b26
"""

import sys
import urllib
import json
import collections

rawdata = urllib.urlopen("http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key="+sys.argv[1]+"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2])
busdata = json.load(rawdata)

print "Bus line: "+sys.argv[2]

# use the number of data objects in vehicle activity to count the number of active buses
print "Number of active buses: "+str(len(busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]))

# find and print every instance of lat and long
coordinates =[]

for i in range(len(busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])):
	coordinates.append((busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"],busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]))

print "Location: Lat/Long"
for i in coordinates:
	print i

# used to get a pretty print of the raw json file
# print json.dumps(busdata, sort_keys=True, indent=4, separators=(',', ': '))
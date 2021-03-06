import pylab as pl
import json
import requests
import urllib as ulr
import numpy as np

import os


import sys
if __name__ =="__main__":
    key = sys.argv[1]
    busline = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + busline

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

print "Bus Line :", busline
bustotal = np.size(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print "Number of Active Buses :",bustotal
for i in range(bustotal):
    lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print "Bus",i+1, "is at latitude", lat,"and longitude",long

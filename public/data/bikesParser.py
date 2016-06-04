# Jason Morris
# Finished
# June 1, 2016

import json, requests
from pyproj import Proj, transform
print('')

#load all json data from json dump
data_in_file = open('bikesIn.json')

dataIn = json.load(data_in_file)

data_in_file.close()

# dictionary to parse as the output json objects
# formatted for a Leaflet.JS marker cluster
dataOut = {}

#create pnyc to convert x y to lat lng 
inProj = Proj(init='epsg:3857')
outProj = Proj(init='epsg:4326')


count = 0
for row in dataIn["features"]:
	x = row['geometry']['x']
	y = row['geometry']['y']

	lon, lat = transform(inProj,outProj,x,y)

	#build the specific attributes of a marker for a single object (row) in the data array of objects
	buildingJson = {}
	buildingJson['layer'] = 'bicycle'
	buildingJson['lat'] = lat
	buildingJson['lng'] = lon

	#specify a specific icon using awesomeMarker
	iconDict = {}
	iconDict['type'] = 'awesomeMarker'
	iconDict['icon'] = 'bicycle'
	iconDict['markerColor'] = 'gray'
	iconDict['iconColor'] = 'white'
	iconDict['prefix'] = 'fa'

	#add icon to this json for this row
	buildingJson['icon'] = iconDict
	
	#create the entry for this row's json and add it to the dataOut json object (dictionary)
	dataOut['bike' + str(count)] = buildingJson;
	count +=1

#open a json data file and write our dataOut json (dictionary) to that file
data_out_file = open('bikesOut.json', 'w')

data_out_json = json.dumps(dataOut, indent=4, sort_keys=True)

data_out_file.write(data_out_json)

data_out_file.close()

print('')
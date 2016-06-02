# Jason Morris
# Finished
# June 1, 2016

import json, requests
print('')

#load all json data from json dump
data_in_file = open('recyclingIn.json')

dataIn = json.load(data_in_file)

data_in_file.close()

# dictionary to parse as the output json objects
# formatted for a Leaflet.JS marker cluster
dataOut = {}

count = 0
for row in dataIn["data"]:

	#build the specific attributes of a marker for a single object (row) in the data array of objects
	buildingJson = {}
	buildingJson['layer'] = 'recycling'
	buildingJson['message'] = row[9]+'<br>'+row[10]+'<br>'+row[20][0]['address']+', '+row[20][0]['city']+', '+row[20][0]['state']+', '+row[20][0]['zip']
	buildingJson['lat'] = float(row[20][1])
	buildingJson['lng'] = float(row[20][2])

	#specify a specific icon using awesomeMarker
	iconDict = {}
	iconDict['type'] = 'awesomeMarker'
	iconDict['icon'] = 'recycle'
	iconDict['markerColor'] = 'green'
	iconDict['iconColor'] = 'white'
	iconDict['prefix'] = 'fa'

	#add icon to this json for this row
	buildingJson['icon'] = iconDict
	
	#create the entry for this row's json and add it to the dataOut json object (dictionary)
	dataOut['recycling' + str(count)] = buildingJson;
	count +=1

#open a json data file and write our dataOut json (dictionary) to that file
data_out_file = open('recyclingOut.json', 'w')

data_out_json = json.dumps(dataOut, indent=4, sort_keys=True)

data_out_file.write(data_out_json)

data_out_file.close()

print('')
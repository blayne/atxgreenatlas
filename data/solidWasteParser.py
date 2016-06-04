# Jason Morris
# Finished
# June 1, 2016

import json, requests
print('')

#load all json data from json dump
data_in_file = open('solidWasteIn.json')

dataIn = json.load(data_in_file)

data_in_file.close()

# dictionary to parse as the output json objects
# formatted for a Leaflet.JS marker cluster
dataOut = {}

count = 0
for location in dataIn["features"]:
	if location["attributes"]['CITY'] == 'AUSTIN':	
		buildingJson = {}
		
		buildingJson['layer'] = 'solid_waste'
		buildingJson['message'] = str(location["attributes"]['LOC_NAME']) + '<br>' + str(location["attributes"]['ADDRESS']) + ' ' + str(location["attributes"]['CITY']) + ' ' + str(location["attributes"]['STATE']) + ' ' + str(location["attributes"]['ZIP'])
		buildingJson['lat'] = float(str(location["attributes"]["LAT_DD"]))
		buildingJson['lng'] = float(str(location["attributes"]["LONG_DD"]))
		
		iconDict = {}
		iconDict['type'] = 'awesomeMarker'
		iconDict['icon'] = 'trash'
		iconDict['markerColor'] = 'brown'
		iconDict['iconColor'] = 'white'
		iconDict['prefix'] = 'fa'
		
		buildingJson['icon'] = iconDict
		
		dataOut['solid_waste' + str(count)] = buildingJson
		count += 1 
		
data_out_file = open('solidWasteOut.json', 'w')

data_out_json = json.dumps(dataOut, indent = 4, sort_keys = True)

data_out_file.write(data_out_json)

data_out_file.close()

print ''
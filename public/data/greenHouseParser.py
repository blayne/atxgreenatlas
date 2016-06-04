# Adrian Leonard
# Finished
# June 1, 2016

import json
print('')

#load all json data from json dump
data_to_match = open('greenHouseIn.json')
conversion_table = open('greenConversionTable.json')

dataIn = json.load(data_to_match)
dataIn2 = json.load(conversion_table)

data_to_match.close()
conversion_table.close()
# dictionary to parse as the output json objects
# formatted for a Leaflet.JS marker cluster
dataOut = {}
uniqueSites = {}
count = 0
for location in dataIn:	
	for site2 in dataIn2:
		if location['tract'] == site2['GEOID']:
			siteIdentity = str(site2['GEOID']) + "*&&*" + str(site2['INTPTLAT']) + "*&&*" + str(site2['INTPTLONG'])
			if siteIdentity not in uniqueSites:
				uniqueSites[siteIdentity] = []
				uniqueSites[siteIdentity].append(location)
			else:
				uniqueSites[siteIdentity].append(location)

for siteIdentity in uniqueSites:
	siteIdentityArray = siteIdentity.split("*&&*")

	buildingJson = {}

	buildingJson['layer'] = 'greenhouse_gas'
	buildingJson['data'] = uniqueSites[siteIdentity]
	buildingJson['message'] = "SITE ID: " + siteIdentityArray[0]
	buildingJson['lat'] = float(siteIdentityArray[1])
	buildingJson['lng'] = float(siteIdentityArray[2])
	buildingJson['enable'] = ['click']
	buildingJson['logic'] = 'emit'

	iconDict = {}
	iconDict['type'] = 'awesomeMarker'
	iconDict['icon'] = 'cloud'
	iconDict['markerColor'] = 'green'
	iconDict['iconColor'] = 'white'
	iconDict['prefix'] = 'fa'

	buildingJson['icon'] = iconDict

	dataOut['greenhouse_gas' + str(count)] = buildingJson
	count += 1 
		
data_out_file = open('greenHouseOut.json', 'w')

data_out_json = json.dumps(dataOut, indent = 4, sort_keys = True)

data_out_file.write(data_out_json)

data_out_file.close()

print ''
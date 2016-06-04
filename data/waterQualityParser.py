# Jason Morris
# Work in progress
# June 1, 2016

import json, requests
print('')

#load all json data from json dump
data_in_file = open('waterQualityRaw.json')

dataIn = json.load(data_in_file)

data_in_file.close()

#form data from waterQualityRaw.json into arrays of objects per-site location
dataOut = {}

for row in dataIn["data"]:
	if '2015' in row[9] and row[8] is not None and row[10] is not None and row[27] is not None and row[28] is not None:
		siteIdentity = "" + str(row[8])+"*&*"+str(row[10])+"*&*"+str(row[27])+"*&*"+str(row[28])

		if siteIdentity not in dataOut:
			dataOut[siteIdentity] = []
			dataOut[siteIdentity].append(row)
		else:
			dataOut[siteIdentity].append(row)

#use formatted data to extract individual markers in the next for loop
dataIn["data"] = dataOut
dataOut = {}
count = 0

for site in dataIn["data"]:
	siteArray = site.split("*&*")

	recordMessage = "Watershed: " + str(siteArray[0]) + ".<br>Site: " + str(siteArray[1])

	buildingJson = {}
	buildingJson['layer'] = 'water_quality'
	buildingJson['message'] = recordMessage
	buildingJson['data'] = dataIn["data"][site]
	buildingJson['lat'] = float(siteArray[2])
	buildingJson['lng'] = float(siteArray[3])
	buildingJson['enable'] = ['click']
	buildingJson['logic'] = 'emit'

	iconDict = {}
	iconDict['type'] = 'awesomeMarker'
	iconDict['icon'] = 'tint'
	iconDict['markerColor'] = 'blue'
	iconDict['iconColor'] = 'white'
	iconDict['prefix'] = 'fa'

	buildingJson['icon'] = iconDict

	dataOut['quality' + str(count)] = buildingJson;
	count +=1

data_out_file = open('waterQualityOut.json', 'w')

data_out_json = json.dumps(dataOut, indent=4, sort_keys=True)

data_out_file.write(data_out_json)

data_out_file.close();
print('')
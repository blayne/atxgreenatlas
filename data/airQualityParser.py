# Jason Morris
# Work in progress
# June 1, 2016

import json, requests
print('')

#load all json data from json dump
data_in_file = open('airQualityIn.json')

dataIn = json.load(data_in_file)

data_in_file.close()

#form data from waterQualityRaw.json into arrays of objects per-site location
dataOut = {}

for row in dataIn:
	if row['locality'] ==  'AUSTIN' :
		siteIdentity = str(row['facility_site_name']) + "*&&*" + str(row['latitude_msr']) + "*&&*" + str(row['longitude_msr'])
		if siteIdentity not in dataOut:
			dataOut[siteIdentity] = []
			dataOut[siteIdentity].append(row)
		else:
			dataOut[siteIdentity].append(row)

#use formatted data to extract individual markers in the next for loop
uniqueDataDict = dataOut
dataOut = {}
count = 0

for site in uniqueDataDict:
	siteArray = site.split("*&&*")

	buildingJson = {}
	buildingJson['layer'] = 'air_quality'
	buildingJson['message'] = "SITE: " + str(siteArray[0])
	buildingJson['data'] = uniqueDataDict[site]
	buildingJson['lat'] = float(siteArray[1])
	buildingJson['lng'] = float(siteArray[2])
	buildingJson['enable'] = ['click']
	buildingJson['logic'] = 'emit'

	iconDict = {}
	iconDict['type'] = 'awesomeMarker'
	iconDict['icon'] = 'cloud'
	iconDict['markerColor'] = 'blue'
	iconDict['iconColor'] = 'white'
	iconDict['prefix'] = 'fa'

	buildingJson['icon'] = iconDict

	dataOut['air' + str(count)] = buildingJson;
	count +=1

data_out_file = open('airQualityOut.json', 'w')

data_out_json = json.dumps(dataOut, indent=4, sort_keys=True)

data_out_file.write(data_out_json)

data_out_file.close();
print('')
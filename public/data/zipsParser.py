# Jason Morris
# Finished
# June 1, 2016

import json, requests
print('')

#load all json data from json dump
data_in_file = open('zipsRaw.json')

dataIn = json.load(data_in_file)

data_in_file.close()

# dictionary to parse as the output json objects
# formatted for a Leaflet.JS marker cluster
dataOut = {}

count = 0
for row in dataIn["data"]:

	#only map zipcodes in Austin
	if row[13] == 'AUSTIN' :
		latlangs = []
		latLangsTemp = row[8][16:-3].split(', ')
		for latlangPair in latLangsTemp:
			latlangPairArray = latlangPair.split(' ')
			latlangPairDict = {}
			latlangPairDict['lat'] = float(latlangPairArray[1])
			latlangPairDict['lng'] = float(latlangPairArray[0])
			latlangs.append(latlangPairDict)

		#build the specific attributes of a marker for a single object (row) in the data array of objects
		buildingJson = {}
		buildingJson['layer'] = 'zips'
		buildingJson['message'] = str(row[12])
		buildingJson['type'] = 'polygon'
		buildingJson['latlngs'] = latlangs
		buildingJson['color'] = '#B0A3FC'
		buildingJson['weight'] =  1.0
		buildingJson['opacity'] = 1.0
		buildingJson['fillOpacity'] = 0.25

		
		#create the entry for this row's json and add it to the dataOut json object (dictionary)
		dataOut['zips' + str(count)] = buildingJson;
		count +=1

#open a json data file and write our dataOut json (dictionary) to that file
data_out_file = open('zipsOut.json', 'w')

data_out_json = json.dumps(dataOut, indent=4, sort_keys=False)

data_out_file.write(data_out_json)

data_out_file.close()

print('')
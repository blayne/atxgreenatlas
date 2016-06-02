# Jason Morris
# Work in progress
# June 1, 2016

import json, requests
print('')

#load all json data from json dump
data_in_file = open('waterQualityIn.json')

dataIn = json.load(data_in_file)

data_in_file.close()

dataOut = {}
noDupsList = []
count = 0
for row in dataIn["data"]:
	dupeStr = str(row[8]+str(row[10:15]))
	if row[27] is not None and row[28] is not None and dupeStr not in noDupsList:
		noDupsList.append(dupeStr)
		buildingJson = {}
		buildingJson['layer'] = 'water_quality'
		buildingJson['message'] = str(row[:])
		#buildingJson['message'] = row[9]+'<br>'+row[10]+'<br>'+row[20][0]['address']+', '+row[20][0]['city']+', '+row[20][0]['state']+', '+row[20][0]['zip']
		buildingJson['lat'] = float(row[27])
		buildingJson['lng'] = float(row[28])

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
# Jason Morris
# Finished
# June 1, 2016
# refer to recyclingParser.py for appropriate documentation

import json, requests
print('')

#load all json data from json dump
data_in_file = open('storageTanksIn.json')

dataIn = json.load(data_in_file)
dataOut = {}

count = 0
for row in dataIn["data"]:
	buildingJson = {}
	buildingJson['layer'] = 'storage_tanks'
	buildingJson['message'] = row[13]+'<br>'+row[15]+(('<br><a href=\"'+row[21]+'\">Council Notes<a>') if len(row[21]) > 5 else '')
	point = row[9].replace("(","").replace(")","").split(" ")
	buildingJson['lat'] = float(point[2])
	buildingJson['lng'] = float(point[1])

	iconDict = {}
	iconDict['type'] = 'awesomeMarker'
	iconDict['icon'] = 'globe'
	iconDict['markerColor'] = 'red'
	iconDict['iconColor'] = 'white'
	iconDict['prefix'] = 'fa'

	buildingJson['icon'] = iconDict
	
	dataOut['storage_tanks' + str(count)] = buildingJson;
	count +=1

data_out_file = open('storageTanksOut.json', 'w')

data_out_json = json.dumps(dataOut, indent=4, sort_keys=True)

data_out_file.write(data_out_json)

data_out_file.close();
data_in_file.close()

print('')
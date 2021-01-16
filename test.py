import json
from collections import OrderedDict

data = json.load(open('gin.data.json'), object_pairs_hook=OrderedDict)

for element in data['elements']:
	suborigin = element['origin'].split(' - ')

	if len(suborigin) == 1:
		element['origin'] = {
			'country': suborigin[0]
		}
	else:
		element['origin'] = {
			'city': suborigin[0],
			'country': suborigin[1]
		}

with open('gin2.data.json', 'w') as file:
	json.dump(data, file, indent='\t')

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"

while True:
	address = input("Enter location: ")
	if len(address)<1: break

	url = serviceurl + urllib.parse.urlencode(
        {'address': address})
	print("Retrieving: ", url)
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	print("Retrieved: ", len(data)," characters")

	try: js = json.loads(data)
	except: js = None

	if 'status' not in js or js['status']!='OK':
		print("---Failure to retrieve ---")
		print (data)
		continue

	# print(json.dumps(js, indent = 4))


	location = js['results'][0]['place_id']
	print (location)

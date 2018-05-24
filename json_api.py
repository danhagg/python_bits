import urllib.parse
import requests

# define url it communicates with at google
main_api = "http://maps.googleapis/maps/api\geocode/json?"

key = '&key=AIzaSyC9JYdnoqoOr7bsUvNnzBs4pQ0IZhd-bSQ'
address = 'lhr'
url = main_api + urllib.parse.urlencode({'address': address}) + key

json_data = requests.get(url).json()
print(json_data)

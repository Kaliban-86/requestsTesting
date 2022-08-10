import requests
import pprint


url = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=faPokcRMMPGmi75N5MKKvALVn5q0OujAF0jeO5ot'
result = requests.get(url).json()
print(type(result))
print(len(result))
#print(result[0])
first_data = result[0]
pprint.pprint(result)
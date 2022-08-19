# import requests
# import pprint
#
#
# url = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=faPokcRMMPGmi75N5MKKvALVn5q0OujAF0jeO5ot'
# result = requests.get(url).json()
# print(type(result))
# print(len(result))
# #print(result[0])
# first_data = result[0]
# pprint.pprint(first_data[caption])

list_list = [5,50]


def some(args):
    a, b = args
    return a, b
print(some(list_list))
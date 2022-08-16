from pycbrf import ExchangeRates
import json
import pprint
# rate = ExchangeRates()

# print(rate['USD'].value)

with open('resul.json', 'r') as f:
    res = json.load(f)

pprint.pprint(res)
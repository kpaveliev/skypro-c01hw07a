import utils
import json

# Read data from a file
cities_file = '01_cities.json'
cities = utils.open_json(cities_file)

# Creating flat dictionary
cities_flat = {}

for item in cities:
    key_ = item['pk']
    cities_flat[key_] = {'name': item['fields']['name'],
                         'timezone': item['fields']['timezone'],
                         'country': item['fields']['country'],
                         'country_ru': item['fields']['country_ru']
                        }

utils.write_to_json('02_flat_cities.json', cities_flat)

# print(cities_flat)
# print(json.dumps(cities_flat, sort_keys=False, indent=4))


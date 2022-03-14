import utils

# Read data from a file
cities_file = '01_cities.json'
cities = utils.open_json(cities_file)

# Creating dictionary of cities by countries
cities_by_countries = {}

for item in cities:
    country = item['fields']['country_ru']
    cities_by_countries[country] = []

for item in cities:
    country = item['fields']['country_ru']
    city = item['fields']['name']
    cities_by_countries[country].append(city)

# Printing results
for country in cities_by_countries:
    character = '\n- '
    print(
        f'{country}:\n'
        f'- '
        f'{character.join(cities_by_countries[country])}'
    )


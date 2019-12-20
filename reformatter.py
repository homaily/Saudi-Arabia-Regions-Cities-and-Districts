import json

cities = json.load(open('./json/cities.json', ))
districts = json.load(open('./json/districts.json'))
regions = json.load(open('./json/regions.json'))


""" remove all cities that has no districts """
# get list of cities that has districts
real_cities = set(map(lambda district: district['city_id'], districts))

# remove cities that has no districts
cities = list(filter(lambda city: city['city_id'] in real_cities, cities))

# update cities file
with open('./json/light_cities.json', 'w') as cities_file:
    cities_file.write(json.dumps(cities, ensure_ascii=False))


""" create new json that structured cities based on their region """
cities_based_on_region = {}

# iterate through all regions
for region in regions:

    # just get the cities for this region
    region_cities = filter(lambda city: city['region_id'] == region['region_id'], cities)

    # fol all cities, don't store all city attributes, just get city name in english and arabic
    region_cities = map(lambda city:
                        {'name_ar': city['name_ar'], 'name_en': city['name_en']}
                        , region_cities)

    # store the region with specific attributes and its cities
    cities_based_on_region[region['region_id']] = {
        'name_ar': region['name_ar'],
        'name_en': region['name_en'],
        'cities': list(region_cities)
    }

# create store the new json in file
with open('./json/citiesBasedOnRegion.json', 'w') as cities_based_on_region_file:
    cities_based_on_region_file.write(json.dumps(cities_based_on_region, ensure_ascii=False))

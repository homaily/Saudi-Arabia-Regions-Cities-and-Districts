# This file takes embeds all cities and district under a region into one file with regions at the top,
# and cities are a field of regions, and districts are a field of cities, all in one file
import json

with open("../json/regions.json") as f:
    __regions_source__ = json.load(f)
with open("../json/cities.json") as f:
    __cities_source__ = json.load(f)
with open("../json/districts.json") as f:
    __districts_source__ = json.load(f)


def __remove_id_fields(x: dict):
    return {k: v for k, v in x.items() if k not in ["region_id", "city_id", "district_id", "capital_city_id"]}


def find_cities_and_capital_city_for_region(p_region_source, cities_source):
    capital_city_id = p_region_source["capital_city_id"]
    cities_under_region = []
    for city in cities_source:
        if city["region_id"] == p_region_source["region_id"]:
            if city["city_id"] == capital_city_id:
                capital_city = __remove_id_fields(city)
            cities_under_region.append(__remove_id_fields(city))

    assert len(cities_under_region) > 0 and capital_city
    return cities_under_region, capital_city


def embed_districts_in_cities():
    embedded_districts_within_cities = []
    for city in __cities_source__:
        city_districts = []
        for district in __districts_source__:
            if district["city_id"] == city["city_id"]:
                city_districts.append(__remove_id_fields(district))
        city["districts"] = city_districts
        embedded_districts_within_cities.append(city)
    return embedded_districts_within_cities


cities_target = embed_districts_in_cities()
regions_target = []

for region_source in __regions_source__:
    region = region_source
    cities, capital_city = find_cities_and_capital_city_for_region(region_source, cities_target)
    region["capital_city"] = capital_city
    region["cities"] = cities
    regions_target.append(__remove_id_fields(region))

with open("../json/embedded_regions.json", 'w') as f:
    json.dump(regions_target, f, ensure_ascii=False)

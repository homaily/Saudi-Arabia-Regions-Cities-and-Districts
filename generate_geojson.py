import json
import geojson
import os
from geojson_rewind import rewind

SOURCE_JSON_FILES = [
    "json/cities.json", "json/districts.json", "json/regions.json"]
OUTPUT_GEOJSON_DIR = "geojson/"


def convert_cities_to_geojson_feature_collection(cities):
    geojson_features = []
    for city in cities:
        center_point = geojson.Point((city["center"][1], city["center"][0]))
        city.pop("center")
        feature = geojson.Feature(geometry=center_point, properties=city)
        geojson_features.append(feature)
    return geojson.FeatureCollection(geojson_features)


# Convert from (latitude, longitude) to (longitude, latitude) format
# Supports any level of nesting
def __flip_coordinates__(coords_array):
    for i in range(len(coords_array)):
        for j in range(len(coords_array[i])):
            coords_array[i][j] = [coords_array[i][j][1], coords_array[i][j][0]]
    return coords_array


def convert_districts_to_geojson_feature_collection(districts):
    geojson_features = []
    for district in districts:
        district_polygon = rewind(geojson.Polygon(__flip_coordinates__(district["boundaries"])))
        district.pop("boundaries")
        district_feature = geojson.Feature(geometry=district_polygon, properties=district)
        geojson_features.append(district_feature)
    return geojson.FeatureCollection(geojson_features)


def convert_regions_to_geojson_feature_collection(regions):
    geojson_features = []
    for region in regions:
        region_boundary_polygon = rewind(geojson.Polygon(__flip_coordinates__(region["boundaries"])))
        region_center_point = geojson.Point((region["center"][1], region["center"][0]))
        region_geometry_collection = geojson.GeometryCollection([region_boundary_polygon, region_center_point])
        region.pop("center")
        region.pop("boundaries")
        region_feature = geojson.Feature(geometry=region_geometry_collection, properties=region)
        geojson_features.append(region_feature)
    return geojson.FeatureCollection(geojson_features)


for source_json_file in SOURCE_JSON_FILES:
    with open(source_json_file) as json_f:
        json_obj = json.load(json_f)
        file_name = os.path.basename(source_json_file)
        if file_name == "cities.json":
            feature_collection = convert_cities_to_geojson_feature_collection(json_obj)
        elif file_name == "districts.json":
            feature_collection = convert_districts_to_geojson_feature_collection(json_obj)
        elif file_name == "regions.json":
            feature_collection = convert_regions_to_geojson_feature_collection(json_obj)
        assert feature_collection
        assert len(feature_collection.errors()) == 0
        geojson_file_name = file_name.replace("json", "geojson")
        geojson_file_path = os.path.join(OUTPUT_GEOJSON_DIR, geojson_file_name)
        with open(geojson_file_path, 'w') as geojson_f:
            geojson.dump(feature_collection, geojson_f, ensure_ascii=False)

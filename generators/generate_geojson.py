import json
import geojson
import os
from geojson_rewind import rewind

SOURCE_JSON_FILES = [
    "../json/cities.json", "../json/districts.json", "../json/regions.json", "../json/embedded_regions.json"
]
OUTPUT_GEOJSON_DIR = "../geojson/"


# Convert from (latitude, longitude) to (longitude, latitude) format
# Supports any level of nesting
def __flip_coordinates__(coords_array):
    if len(coords_array) == 2 and \
            (isinstance(coords_array[0], float) or isinstance(coords_array[0], int)):
        return [coords_array[1], coords_array[0]]
    return [__flip_coordinates__(nested_arr) for nested_arr in coords_array]


def convert_cities_to_geojson_feature_collection(cities):
    geojson_features = []
    for city in cities:
        center_point = geojson.Point((city["center"][1], city["center"][0]))
        city.pop("center")
        feature = geojson.Feature(geometry=center_point, properties=city)
        geojson_features.append(feature)
    return geojson.FeatureCollection(geojson_features)


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


def convert_embedded_regions_to_geojson_feature_collection(embedded_regions_json):
    geojson_features = []
    for region in embedded_regions_json:
        top_geometry_collection = [
            rewind(geojson.Polygon(__flip_coordinates__(region["boundaries"])))
        ]
        region_cities_cords = []
        cities_districts = []
        for city in region["cities"]:
            cords_flipped = __flip_coordinates__(city["center"])
            region_cities_cords.append((cords_flipped[0], cords_flipped[1]))
            cities_districts += [__flip_coordinates__(district["boundaries"]) for district in city["districts"]]

        top_geometry_collection.append(geojson.MultiPoint(region_cities_cords))
        top_geometry_collection.append(rewind(geojson.MultiPolygon(cities_districts)))
        geojson_features.append(geojson.Feature(geometry=geojson.GeometryCollection(top_geometry_collection)))
        # break

    return geojson.FeatureCollection(geojson_features)


for source_json_file in SOURCE_JSON_FILES:
    if not os.path.exists(source_json_file):
        print(f"{source_json_file} does not exist. Skipping ...")
        continue
    print(f"Converting {source_json_file} to geojson...")
    with open(source_json_file) as json_f:
        json_obj = json.load(json_f)
        file_name = os.path.basename(source_json_file)
        if file_name == "cities.json":
            feature_collection = convert_cities_to_geojson_feature_collection(json_obj)
        elif file_name == "districts.json":
            feature_collection = convert_districts_to_geojson_feature_collection(json_obj)
        elif file_name == "regions.json":
            feature_collection = convert_regions_to_geojson_feature_collection(json_obj)
        elif file_name == "embedded_regions.json":
            feature_collection = convert_embedded_regions_to_geojson_feature_collection(json_obj)
        assert feature_collection
        assert len(feature_collection.errors()) == 0
        geojson_file_name = file_name.replace("json", "geojson")
        geojson_file_path = os.path.join(OUTPUT_GEOJSON_DIR, geojson_file_name)
        with open(geojson_file_path, 'w') as geojson_f:
            geojson.dump(feature_collection, geojson_f, ensure_ascii=False)

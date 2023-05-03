import geojson
from shapely.geometry import Point, Polygon, MultiPolygon

# Load the GeoJSON data from a file or URL
with open('mm.geojson') as f:
    data = geojson.load(f)

# Define the location as a (longitude, latitude) tuple
location = (97.0450431,21.5079406)


# Iterate through the features and check if the location is within the bounds of the feature's geometry
for feature in data['features']:
    if feature['geometry']['type'] == 'Point':
        if tuple(feature['geometry']['coordinates']) == location:
            # If the location matches a Point feature, retrieve the properties of the feature
            properties = feature['properties']
            print(properties)
    elif feature['geometry']['type'] == 'Polygon':
        polygon = Polygon(feature['geometry']['coordinates'][0])
        if polygon.contains(Point(location)):
            # If the location is within the bounds of a Polygon feature, retrieve the properties of the feature
            properties = feature['properties']
            print(properties)
    elif feature['geometry']['type'] == 'MultiPolygon':
        
        for polygon_coords in feature['geometry']['coordinates']:
            
            polygon = Polygon(polygon_coords[0])
            if polygon.contains(Point(location)):
                # If the location is within the bounds of a MultiPolygon feature, retrieve the properties of the feature
                properties = feature['properties']
                print(properties)
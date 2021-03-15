import csv, json
from geojson import Feature, FeatureCollection, Point

features = []
with open('data/Book2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for y, x, market, desc in reader:
        print(type(float(y)))
        latitude, longitude = map(float, (float(x), float(y)))
        features.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'market': market,
                    'desc': desc
                }
            )
        )

# collection = FeatureCollection(features)
# with open("GeoObs.json", "w") as f:
#     f.write('%s' % collection)
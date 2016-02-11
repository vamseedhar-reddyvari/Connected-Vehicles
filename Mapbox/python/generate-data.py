import geojson as geo

Center = (-83.79706,42.268138)
Center_Point = geo.Point(Center)

# Create feature and collection
f = geo.Feature(geometry=Center_Point,properties='Center')
F = geo.FeatureCollection([f])

# generate data
geo_data_str = geo.dumps(F,sort_keys=True)


# Write into file
json_file  = open('../data/center-point.json','w')
json_file.write(geo_data_str)
json_file.close()

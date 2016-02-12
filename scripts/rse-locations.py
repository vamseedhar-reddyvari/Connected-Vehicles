__author__ = 'vamsee'

import geojson as geo

Center = (-83.79706,42.268138)
Center_Point = geo.Point(Center)

def get_locations(filename,lat_idx,long_idx, write_filename,point_properties):
    opened_file = open(filename)
    features_list = []
    for line in opened_file:
        line_contents = line.split(',')
        (longitude,latitude) = (float(line_contents[lat_idx])/10000000,float(line_contents[long_idx])/10000000 )
        f = geo.Feature(geometry=geo.Point( (longitude,latitude)), \
            properties = point_properties )
        features_list.append(f)
        #break
    F = geo.FeatureCollection(features_list)
    # generate data
    geo_data_str = geo.dumps(F,sort_keys=True)


    # Write into file
    json_file  = open('../Mapbox/data/'+write_filename,'w')
    json_file.write(geo_data_str)
    json_file.close()




# get_locations('../../Transportation-Data/Data/RSE_BSM/RSE_BSM_trimmed.csv')
get_locations('../BSM-RSE.csv',7,6,'vehicle-locations.json',{'title':'Vehicle Location',  "marker-symbol": "car", "marker-size": "medium", "marker-color": "#09f"})
get_locations('../Geometry.csv',4,3,'rse-data-locations.json',{'title':'RSE Location',  "marker-symbol": "commercial", "marker-size": "large", "marker-color": "#f83"})

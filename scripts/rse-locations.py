__author__ = 'vamsee'

import geojson as geo

Center = (-83.79706,42.268138)
Center_Point = geo.Point(Center)








def get_locations(filename):
    opened_file = open(filename)
    features_list = []
    for line in opened_file:
        line_contents = line.split(',')
        (longitude,latitude) = (float(line_contents[7])/10000000,float(line_contents[6])/10000000 )
        f = geo.Feature(geometry=geo.Point( (longitude,latitude)),properties='RX Pnt')
        features_list.append(f)
        #break
    F = geo.FeatureCollection(features_list)
    # generate data
    geo_data_str = geo.dumps(F,sort_keys=True)


    # Write into file
    json_file  = open('../Mapbox/data/rse-data-locations.json','w')
    json_file.write(geo_data_str)
    json_file.close()





get_locations('../../Transportation-Data/Data/RSE_BSM/RSE_BSM_trimmed.csv')

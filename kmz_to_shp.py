


import geopandas as gpd
import fiona

fiona.drvsupport.supported_drivers['libkml'] = 'rw' # enable KML support
fiona.drvsupport.supported_drivers['LIBKML'] = 'rw' # enable KML support 
# Read the KML file 
kmz_file = "columbia_university_zone.kmz"
gdf = gpd.read_file(kmz_file, driver='KMZ')

# GeoDataFrame to a shapefile
shp_file = "columbia_university_zone.shp"
gdf.to_file(shp_file, driver='ESRI Shapefile')
print(gdf)
gdf = gpd.read_file("columbia_university_zone.shp")
print(gdf)

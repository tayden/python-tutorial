import fiona # Reads spatial data formats
import pprint # "Pretty print" - Just print out lists and dictionaries in a nicer format, could use print instead

fires = fiona.open("./data/prot_current_fire_points.shp")

pprint.pprint(fires[0:2])
print
print
print fires[0]['properties']['ZONE']

fires.close() # Good practice to close files if you open them

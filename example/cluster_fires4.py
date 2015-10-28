import fiona
import pprint
from sklearn.cluster import KMeans # KMeans object

fires = fiona.open("./data/prot_current_fire_points.shp")

# Setup KMeans object following scikit-learn documentation
k_means = KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1)

# Get coordinates for each fire in a list
fire_coords = [fire['geometry']['coordinates'] for fire in fires]

# Fit our data to the initialized KMeans object (referenced by k_means variable)
model = k_means.fit(fire_coords)

# Print the clusters for each fire
for fire in fires:
    print "id:", fire['id'], ", cluster:", model.predict(fire['geometry']['coordinates'])

# Note, fit then predict can be combine with the fit_predict function that scikit has...

# NEXT:
#   * Plot with Matplotlib
#   * Use Fiona to export the shapefile
#   * Improve model using PCA, crossvalidation, etc.

fires.close() # Good practice to close files if you open them

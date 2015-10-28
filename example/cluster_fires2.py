import fiona
import pprint
from sklearn.cluster import KMeans # KMeans object

fires = fiona.open("./data/prot_current_fire_points.shp")

# Setup KMeans object following scikit-learn documentation
k_means = KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1)

# Fit our data to the initialized KMeans object (referenced by k_means variable)
k_means.fit(fires) #FAILS

fires.close() # Good practice to close files if you open them

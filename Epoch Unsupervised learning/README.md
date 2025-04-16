This project performs unsupervised clustering of geographical coordinates (latitude and longitude points) from the state of Karnataka, India, using the K-Means algorithm. 
To group spatial data points into meaningful clusters without prior labeling — useful for applications such as region-based analysis, delivery zone optimization, and location-based services.

The K-Means algorithm works as follows:

Initialization:
Randomly choose K centroids on the map.

Assignment Step:
Assign each data point to the nearest centroid based on Euclidean distance.

Update Step:
Recalculate the centroids as the mean of all points assigned to each cluster.

Repeat:
Continue this process until the change (shift) in centroids is negligible or below a set threshold.

Input
A set of latitude and longitude points (e.g., cities or coordinates in Karnataka)

Output
Clusters of data points, each associated with a specific centroid

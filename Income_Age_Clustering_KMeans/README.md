## Income and Age Clustering with KMeans

This Jupyter Notebook explores customer segmentation by income and age using KMeans clustering. It analyzes the "income_age_clustering_data.csv" dataset containing customer age and income information.

**Task:**

Perform KMeans clustering to group customers into distinct clusters based on their income and age.

**Steps Performed:**

1. **Data Loading and Preprocessing:**
   - Loads the CSV data using pandas.
   - Assumes minimal preprocessing is required as features are numerical (Age, Income).

2. **KMeans Clustering:**
   - Initializes a KMeans model with a specified number of clusters (**k**).
   - Fits the model on the customer age and income data.
   - Assigns each customer to a cluster based on their income and age proximity to the cluster centroids.

3. **Evaluation:**
   - Calculates the Silhouette score to assess the quality of the clustering (higher score indicates better separation).
   - Visualizes the data points colored by their assigned cluster labels.

**Experimentation:**

- Explore different values for the number of clusters (**k**) and observe the impact on cluster formation and Silhouette score.
- Try other clustering algorithms like Hierarchical clustering or Density-Based Spatial Clustering of Applications with Noise (DBSCAN).
- Visualize the clusters in a 3D plot if additional features are available.

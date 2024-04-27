## Income and Age Clustering with DBSCAN

This Jupyter Notebook tackles customer segmentation by income and age using the DBSCAN clustering algorithm. It analyzes the "income_age_clustering_data.csv" dataset containing customer age and income information.

**Task:**

Perform DBSCAN clustering to identify clusters of customers with similar income and age characteristics, handling potential outliers.

**Steps Performed:**

1. **Data Loading and Preprocessing:**
   - Loads the CSV data using pandas.
   - Selects Age and Income features for clustering.
   - Applies StandardScaler to normalize the features for better distance calculations in DBSCAN.

2. **DBSCAN Clustering:**
   - Initializes a DBSCAN model with two key parameters:
     - **eps (epsilon):** Maximum distance between two points to be considered in a cluster.
     - **min_samples (minimum samples):** Minimum number of points within an eps-distance to form a cluster.
   - Fits the model on the scaled customer age and income data.
   - Identifies dense regions (clusters) of data points and labels outliers as noise.

3. **Evaluation and Visualization:**
   - Calculates the Silhouette score to assess the quality of the clustering.
   - Visualizes the data points colored by their assigned cluster labels, highlighting outliers.

**Experimentation:**

- Explore different values for **eps** and **min_samples** to observe how they influence cluster formation and outlier detection.
- Compare the results with KMeans clustering from a previous analysis.

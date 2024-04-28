## K-Means vs. DBSCAN Clustering

This Jupyter Notebook explores and compares K-Means and DBSCAN, two popular clustering algorithms. It uses a synthetic dataset with well-defined clusters for visualization purposes.

**Task:**

Compare the performance and applicability of K-Means and DBSCAN for data clustering.

**Steps Performed:**

1. **Synthetic Dataset Generation:**
   - Generates a 2-dimensional dataset with 4 clusters using `make_blobs` from scikit-learn.

2. **K-Means Clustering:**
   - Implements K-Means clustering with varying numbers of clusters (2, 3, and 4).
   - Visualizes the clusters for each K value using Matplotlib.
   - Calculates the Silhouette score to evaluate cluster quality.
   - Identifies the optimal number of clusters based on the Silhouette score.

3. **DBSCAN Clustering:**
   - Implements DBSCAN clustering with different hyperparameter combinations (eps and min_samples).
   - Visualizes the resulting clusters for each parameter setting.
   - Analyzes the impact of eps and min_samples on cluster formation and outlier detection.

4. **Comparison and Insights:**
   - Discusses the strengths and weaknesses of K-Means and DBSCAN.
   - Highlights K-Means' limitations in handling non-spherical clusters and outliers.
   - Emphasizes DBSCAN's advantage in identifying outliers and its flexibility in cluster shapes.

**Experimentation:**

- Try DBSCAN with different distance metrics (e.g., Manhattan distance) to observe effects on clustering.
- Apply K-Means and DBSCAN to real-world datasets to assess their effectiveness in practical scenarios.


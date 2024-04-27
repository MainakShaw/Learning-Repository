## Cancer Cell Classification with PCA

This Jupyter Notebook investigates the impact of Principal Component Analysis (PCA) on cancer cell classification. It performs dimensionality reduction on a dataset containing features of cancer cells and analyzes the effect on classification accuracy.

**Tasks Performed:**

1. **Data Loading and Preprocessing:**
   - Loads the CSV data using pandas.
   - Handles any necessary data cleaning and preprocessing steps.

2. **Train-Test Split:**
   - Splits the data into training and testing sets (80/20 ratio) using `train_test_split`.

3. **Dimensionality Reduction with PCA:**
   - Applies PCA to transform the original features into a lower-dimensional space.
   - Explores the choice of the number of principal components to retain.

4. **Classification Model (Replace with the chosen model):**
   - Trains a classification model (e.g., SVM, Logistic Regression) on the transformed data (after PCA).
   - Evaluates the model's performance on the testing data using appropriate metrics (e.g., accuracy score).

**Key Points:**

- PCA can reduce the complexity of data by identifying the most significant features.
- The choice of the number of principal components can influence classification accuracy.

**Experimentation:**

- Explore different hyperparameter tuning strategies for the chosen classification model.
- Try various techniques for selecting the optimal number of principal components.
- Visualize the data distribution in the original and transformed feature spaces using PCA.


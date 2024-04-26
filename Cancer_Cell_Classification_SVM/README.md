## Cancer Cell Classification with Support Vector Machines

This Jupyter Notebook explores Support Vector Machine (SVM) classification for identifying cancer types in cells based on the "cell_samples.csv" dataset.

**Tasks Performed:**

1. **Data Loading and Preprocessing:**
    - Loads the CSV data using pandas.
    - Checks for missing values and handles them by replacing '?' with '0' and converting the column to integer type.
    - Drops the ID column as it's not relevant for classification.
    - Identifies features (X) and target class (y).

2. **Train-Test Split:**
    - Splits the data into training and testing sets (80/20 ratio) using `train_test_split` from scikit-learn.

3. **Model Training and Evaluation:**
    - Trains SVM models with different kernel functions (linear, polynomial, RBF, sigmoid) using `SVC` from scikit-learn.
    - Evaluates each model's performance on the testing data using accuracy score.
    - Prints the accuracy scores to compare the performance of different kernels.

**Key Points:**

- SVM is a powerful machine learning algorithm for classification tasks.
- Choosing the appropriate kernel function can significantly impact model performance.

**Experimentation:**

- Try different hyperparameter settings for the SVM models.
- Explore other classification algorithms (e.g., decision trees, random forests) and compare their performance.
- Visualize the data distribution and decision boundaries of the SVM models.


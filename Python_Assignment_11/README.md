## Credit Card Fraud Detection with Logistic Regression and SVM

This Jupyter Notebook explores credit card fraud detection using Logistic Regression (LR) and Support Vector Machine (SVM) algorithms. It evaluates the performance of both models on the "creditcardfraud.csv" dataset.

**Tasks Performed:**

1. **Data Loading and Preprocessing:**
    - Loads the CSV data using pandas.
    - Drops the "Time" column as it's not relevant for classification.
    - Applies StandardScaler to normalize the "Amount" column.

2. **Train-Test Split:**
    - Splits the data into training and testing sets (80/20 ratio) using `train_test_split` with `random_state=42` for reproducibility.

3. **Logistic Regression:**
    - Trains a baseline Logistic Regression model with default hyperparameters.
    - Evaluates the model's performance on the test set using confusion matrix and classification report.
    - Performs GridSearchCV to find the optimal hyperparameters for Logistic Regression.
    - Trains the model again with the best hyperparameters and re-evaluates.

4. **Support Vector Machine (SVM):**
    - Trains a baseline SVM model with default hyperparameters.
    - Evaluates the model's performance on the test set using confusion matrix and classification report.
    - Performs GridSearchCV to find the optimal hyperparameters for SVM.
    - Trains the model again with the best hyperparameters and re-evaluates.

5. **Comparison and Conclusion:**
    - Compares the performance of LR and SVM models based on accuracy scores.
    - Analyzes the potential reasons for differences in performance.

**Key Points:**

- Logistic Regression is a good choice for linear relationships between features and target variables.
- SVM can handle non-linear relationships and potentially outperform LR in such cases.

**Experimentation:**

- Explore different hyperparameter tuning strategies for both models.
- Try other classification algorithms like Random Forest or Gradient Boosting.
- Visualize feature distributions to understand class separation.


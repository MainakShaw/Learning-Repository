## Energy Efficiency: Multi-Linear & Polynomial Regression

This Jupyter Notebook investigates multi-linear and polynomial regression models for predicting building heating load (target variable) using the "Energy Dataset.xlsx" file. 

**Key Steps:**

1. **Data Loading and Preprocessing:**
    - Loads the Excel data using pandas.
    - Verifies the absence of null values and constant features.
    - Identifies (no) categorical columns for encoding.
    - Scales numerical features using StandardScaler for better model performance.

2. **Feature Engineering (Polynomial Regression):**
    - Utilizes `PolynomialFeatures` to transform existing features into polynomial features (degree 2).
    - Creates a new DataFrame with transformed features and column names.

3. **Model Training and Evaluation:**
    - Splits the data into training and testing sets (80/20 ratio).
    - Trains multi-linear and polynomial regression models using `LinearRegression`.
    - Evaluates both models using R-squared and mean squared error (MSE) on the testing data.
    - Prints the evaluation metrics to compare model performance.

4. **Analysis and Conclusion:**
    - Observes the improvement in R-squared and decrease in MSE for polynomial regression.
    - Concludes that polynomial regression provides a better fit for this dataset.

**Benefits:**

- Demonstrates multi-linear and polynomial regression in a practical energy efficiency prediction scenario.
- Highlights the importance of data preprocessing and feature engineering for improved model performance.
- Provides a foundation for exploring different polynomial degrees and hyperparameter tuning.

**Getting Started:**

1. Download the Jupyter Notebook file.
2. Open the notebook in a Jupyter Notebook environment.
3. Run the code cells sequentially to understand the energy efficiency prediction process.

**Experimentation:**

- Explore different polynomial degrees and compare their performance.
- Implement hyperparameter tuning techniques to optimize model performance.
- Visualize the relationship between features and heating load.

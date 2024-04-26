## Predicting Ice Cream Sales with Linear Regression

This Jupyter Notebook explores linear regression models for predicting ice cream sales based on temperature data in the "IceCreamSales.csv" dataset.

**Approaches Explored:**

1. **Linear Regression:**
    - Trains a simple linear regression model using temperature as the independent variable.
    - Evaluates the model's performance using R-squared score and visualizes the predicted vs. actual sales.

2. **Polynomial Regression with Feature Transformation:**
    - Transforms the temperature feature using polynomial features of degree 2 and 3.
    - Trains linear regression models on the transformed features to capture non-linear relationships.

3. **Polynomial Regression with Pipeline:**
    - Utilizes a `PolynomialFeatures` transformer to create higher-order features directly within the linear regression pipeline.
    - Optimizes the code for a more concise approach.

**Key Takeaways:**

- Linear regression can be a good starting point for modeling ice cream sales with temperature.
- Polynomial regression can potentially improve model accuracy by capturing non-linear trends.
- The choice of polynomial degree needs to be balanced to avoid overfitting.

**Getting Started:**

1. Download the Jupyter Notebook file.
2. Open the notebook in a Jupyter Notebook environment.
3. Run the code cells sequentially to explore different linear regression approaches for ice cream sales prediction.

**Experimentation:**

- Try different polynomial degrees and compare their performance.
- Visualize the distribution of sales data.

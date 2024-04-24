## Mobile Price Prediction with Feature Selection using MIR

This Jupyter Notebook tackles mobile price prediction using a machine learning approach. It emphasizes the importance of feature selection and demonstrates its application with Mutual Information Regression (MIR) from scikit-learn.

**The notebook covers:**

* **Mobile Price Prediction Overview:** Understand the task of predicting mobile phone prices based on various features.
* **Data Cleaning and Preprocessing:** Learn techniques like handling missing values, converting data types, and label encoding categorical features for machine learning compatibility.
* **Feature Selection with MIR:** Discover Mutual Information Regression (MIR) and its role in identifying informative features for price prediction.
* **Exploratory Data Analysis (EDA):** Gain insights into the data through visualizations.

**Learning Outcomes:**

* Gain a practical understanding of mobile price prediction with machine learning.
* Apply data cleaning and preprocessing techniques for real-world datasets.
* Utilize MIR for feature selection to potentially improve model performance.

**Notebook Structure:**

The notebook utilizes the "mobile_prices_2023.csv" dataset for the following steps:

1. **Data Loading and Exploration:** Load the dataset and analyze initial data.
2. **Data Cleaning:** Handle missing values, remove irrelevant columns, and address data type inconsistencies.
3. **Feature Preprocessing:** Encode categorical features using Label Encoding.
4. **Feature Selection with MIR:** Calculate MIR scores to identify features with high dependency on price.
5. **Visualization:** Visualize MIR scores to understand feature importance (e.g., bar chart).

**Getting Started:**

1. Download the Jupyter Notebook file.
2. Open the notebook in a Jupyter Notebook environment.
3. Run the code cells sequentially to explore data cleaning, feature selection with MIR, and experiment with different visualizations.

**Feel free to:**

* Use a different dataset containing mobile phone specifications and prices.
* Implement a machine learning model for mobile price prediction (e.g., linear regression) after feature selection.
* Explore additional feature selection techniques (e.g., correlation analysis).

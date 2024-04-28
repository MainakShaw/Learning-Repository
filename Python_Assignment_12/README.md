## Bank Marketing Classification

This Jupyter Notebook tackles customer classification for term deposit subscription prediction in the bank marketing dataset. It explores three machine learning models: Decision Tree Classifier, Random Forest Classifier, and XGBoost Classifier.

**Task:**

Predict whether a customer will subscribe to a term deposit based on their bank account details.

**Steps Performed:**

1. **Data Loading and Preprocessing:**
   - Loads the "bank.csv" dataset using pandas.
   - Handles missing values (there are none in this case).
   - Encodes categorical features using One-Hot Encoding.
   - Scales numerical features using StandardScaler for better model performance.
   - Transforms the target variable ("y") from categorical to numerical ("no" -> 0, "yes" -> 1).

2. **Train-Test Split:**
   - Splits the data into training and testing sets (70/30 ratio) using `train_test_split`.

3. **Model Building and Evaluation:**
   - Trains three classification models:
     - Decision Tree Classifier
     - Random Forest Classifier (with 100 estimators)
     - XGBoost Classifier
   - Evaluates each model on the testing set using accuracy, precision, recall, and F1-score (for both classes).
   - Visualizes the model performance comparisons using Seaborn bar charts.

4. **Insights:**
   - Analyzes the impact of class imbalance on model performance.
   - Identifies the model with the most balanced performance across classes.

**Experimentation:**

- Explore hyperparameter tuning for each model to potentially improve performance.
- Consider using SMOTE (Synthetic Minority Oversampling Technique) to address class imbalance.
- Evaluate additional classification algorithms like Support Vector Machines (SVM).

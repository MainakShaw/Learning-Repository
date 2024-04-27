## Drug Classification with Machine Learning Algorithms

This Jupyter Notebook explores the classification of drugs based on patient characteristics using various machine learning algorithms. It analyzes the "drug200.csv" dataset containing patient information and corresponding drug types.

**Algorithms Investigated:**

- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier
- K-Nearest Neighbors (KNN)

**Tasks Performed:**

1. **Data Loading and Preprocessing:**
    - Loads the CSV data using pandas.
    - Handles categorical features using One-Hot Encoding for Sex and label encoding for Drug types.
    - Maps string values for Blood Pressure and Cholesterol to numerical values.
    - Splits the data into training and testing sets (80/20 ratio) using `train_test_split`.

2. **Model Training and Evaluation:**
    - Trains each model (Decision Tree, Random Forest, XGBoost, KNN) on the training data.
    - Evaluates the performance of each model on the testing data using accuracy score.

**Key Points:**

- Different machine learning algorithms can achieve varying performance on classification tasks.
- Feature engineering techniques like encoding can improve model performance.

**Experimentation:**

- Tune hyperparameters for each model to potentially improve accuracy.
- Explore other classification algorithms like Support Vector Machines (SVM).
- Visualize feature distributions to understand their influence on drug classification.
- 

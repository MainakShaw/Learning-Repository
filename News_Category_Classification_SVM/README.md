## News Category Classification with SVM

This Jupyter Notebook tackles news article classification using a Support Vector Machine (SVM) with a linear kernel. It demonstrates the process on the "BBC News Train.csv" dataset.

**Tasks Performed:**

1. **Data Loading and Preprocessing:**
    - Loads the CSV data using pandas.
    - Focuses on the text (`Text`) and category labels (`Category`).

2. **Feature Extraction:**
    - Applies TF-IDF vectorization to transform news article text into numerical features.
    - TF-IDF captures the importance of words based on their document and corpus frequency.

3. **Train-Test Split:**
    - Splits the data into training and testing sets (80/20 ratio) using `train_test_split` from scikit-learn.

4. **Model Training and Evaluation:**
    - Trains an SVM model with a linear kernel to classify news articles into predefined categories.
    - Evaluates the model's performance on the testing data using accuracy score.

5. **User Input Prediction:**
    - Allows users to input news article text for category prediction using the trained model.

**Key Points:**

- SVM is a powerful machine learning algorithm for text classification tasks.
- TF-IDF helps identify informative keywords for news article categorization.

**Experimentation:**

- Explore different SVM kernel functions (e.g., RBF) and compare their performance.
- Try other feature extraction techniques like Bag-of-Words or Word2Vec.
- Visualize the TF-IDF weights for a better understanding of category-specific keywords.

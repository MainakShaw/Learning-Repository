## Sentiment Analysis with SVM Classification

This Jupyter Notebook explores sentiment analysis of text data using a Support Vector Machine (SVM) with a linear kernel. It demonstrates the process on a sentiment analysis dataset (`Sentiment Analysis Dataset.csv`).

**Steps Performed:**

1. **Data Loading and Preprocessing:**
    - Loads the CSV data using pandas.
    - Handles missing values by dropping rows with NaN values.
    - Applies TF-IDF vectorization to transform text data into numerical features.

2. **Train-Test Split:**
    - Splits the data into training and testing sets (80/20 ratio) using `train_test_split` from scikit-learn.

3. **Model Training and Evaluation:**
    - Trains an SVM model with a linear kernel for sentiment classification (`positive` or `negative`).
    - Evaluates the model's performance on the testing data using accuracy score and classification report.

4. **User Input Prediction:**
    - Allows users to input text for sentiment prediction using the trained model.

**Key Points:**

- TF-IDF helps capture the importance of words based on their document and corpus frequency.
- SVM is a powerful machine learning algorithm for text classification tasks.

**Experimentation:**

- Try different feature extraction techniques like Bag-of-Words or Word2Vec.
- Explore other SVM kernel functions (e.g., RBF) and compare their performance.
- Visualize the TF-IDF weights for better understanding of feature importance.

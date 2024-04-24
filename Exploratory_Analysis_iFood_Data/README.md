## Exploratory Data Analysis of iFood Marketing Data

This Jupyter Notebook explores a marketing dataset obtained from Kaggle using the `opendatasets` library. The data contains information about customer demographics and spending habits on the iFood platform.

**Analysis Steps:**

1. **Data Acquisition:** Downloads the iFood marketing dataset from Kaggle using `opendatasets`.
2. **Data Cleaning and Exploration:**
   - Checks for missing values and data types.
   - Analyzes basic statistics using `describe()`.
   - Creates new income ranges using `pd.cut()`.
3. **Customer Base Analysis:**
   - Groups customers by income ranges and calculates the distribution.
   - Visualizes customer distribution using Seaborn's bar plot.
   - Creates a function `customer_base_based_on_income_func` for reusability.
4. **Feature Analysis:**
   - Analyzes the distribution of "Kidhome" and "Teenhome" features (number of kids and teens at home).
   - Visualizes the distribution using Seaborn's bar plot.
   - Creates pivot tables to explore the relationship between these features and "MntTotal" (total spending).
5. **Campaign Analysis:**
   - Analyzes the sum of accepted campaigns for each customer.
   - Visualizes the acceptance scores for each campaign using Seaborn's bar plot.
6. **Scatter Plot Analysis:**
   - Creates scatter plots to explore the relationships between "MntWines" (wine spending) and other variables like "MntTotal" (total spending) and "MntFruits" (fruit spending).

**Libraries Used:**

* pandas
* opendatasets (for data acquisition)
* seaborn (for data visualization)
* matplotlib.pyplot (for additional plot customization)

**Dataset Source:**

* Kaggle: https://www.kaggle.com/datasets/jackdaoud/marketing-data (link might change)

This project demonstrates the initial stages of exploratory data analysis using Python libraries. Feel free to modify and extend the analysis based on your interests and insights!

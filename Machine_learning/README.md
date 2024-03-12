# Supervised Learning - Predicting Boston House Prices
![image](https://github.com/Blaqdiana/Machine-Learning/assets/109005502/7a3d22fc-b1a3-49ab-90ba-de24d6d5cc0a)

## Project Overview
1. #### Introduction:  
   The aim of this project is to leverage supervised learning techniques to predict house prices in the city of Boston. The dataset used for this analysis is the well-known Boston Housing dataset,which contains various
   features related to housing in different neighborhoods.  
Data Source: [Boston Housing dataset](https://www.kaggle.com/c/boston-housing) available on Kaggle or directly from scikit-learn.
   
2. #### Data Exploration:  
   The project begins with the exploration of the Boston Housing dataset. Exploratory Data Analysis (EDA) is conducted to understand the structure, characteristics, and distribution of the data. This step involves handling
   missing values, checking for outliers, and gaining insights into the relationships between different variables.

3. #### Features and Target Variable:
   The dataset includes multiple features such as crime rate, average number of rooms, proximity to employment centers, etc. The target variable is the median value of owner-occupied homes in thousands of dollars. Identifying
   the relevant features and understanding their impact on the target variable is crucial for building effective predictive models.

4. #### Data Splitting:
   To assess the performance of the machine learning models, the dataset is divided into training and testing sets. The training set is used to train the models, while the testing set is reserved for evaluating their performance 
   on unseen data. This split helps ensure that the models generalize well to new, unseen instances.

5. #### Machine Learning Models:
   Two supervised machine learning models are employed for predicting house prices:

   - Linear Regression: A model that assumes a linear relationship between the input features and the target variable.
   - Decision Tree: A tree-based model that makes predictions based on a series of binary decisions.

6. #### Model Evaluation:
   The performance of the models is assessed using relevant evaluation metrics such as:

    - Root Mean Squared Error (RMSE): Measures the average magnitude of the errors between predicted and actual values.
    - R-squared (R²): Indicates the proportion of the variance in the target variable that is predictable from the independent variables.

## Conclusion
   The objective of this project is to identify the model that provides the most accurate and reliable predictions for house prices in Boston.
### Note:
* The results and findings from this analysis can be used to assist real estate stakeholders, policymakers, and individuals in making informed decisions related to housing in Boston.

### Running the program:
The file Boston_housing.ipynb is a jupiter notebook and it can be ran on Anaconda, google colab or any IDE that supports jupiter notebooks or lab

### Requirements:
Language: Python 3.10 or above  
Libraries: pandas, Numpy, Sklearn

### Built with:
IDE : Visual Studio Code

### Date of Project Submission:
--Date created: 12/01/2024

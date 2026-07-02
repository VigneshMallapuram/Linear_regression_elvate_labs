# Linear Regression - House Price Prediction

## Overview

This project demonstrates the implementation of **Simple Linear Regression** and **Multiple Linear Regression** using Python and Scikit-learn. The objective is to predict house prices based on various features from the Housing dataset.

The project covers the complete machine learning workflow, including data preprocessing, model training, prediction, evaluation, and visualization.

---

## Objective

- Implement Simple Linear Regression.
- Implement Multiple Linear Regression.
- Understand the workflow of a regression model.
- Evaluate model performance using standard regression metrics.
- Visualize the regression line.
- Interpret regression coefficients.

---

## Dataset

**Dataset Used:** Housing Price Prediction Dataset (`Housing.csv`)

The dataset contains the following features:

- Price
- Area
- Bedrooms
- Bathrooms
- Stories
- Main Road Access
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Parking
- Preferred Area
- Furnishing Status

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

# Project Workflow

## 1. Import Libraries

Import the required libraries for data manipulation, visualization, and machine learning.

---

## 2. Load Dataset

Load the Housing dataset using Pandas and inspect the data.

---

## 3. Data Preprocessing

- Handle categorical variables.
- Convert **Yes/No** values into numerical format.
- Apply One-Hot Encoding to categorical columns.
- Separate features and target variable.

---

## 4. Train-Test Split

Split the dataset into:

- **80% Training Data**
- **20% Testing Data**

This allows the model to learn from one portion of the data and evaluate its performance on unseen data.

---

## 5. Model Training

### Simple Linear Regression

A Simple Linear Regression model is trained using **Area** as the independent variable to predict house prices.

**Formula:**

\[
y = mx + c
\]

Where:

- **y** = Predicted house price
- **x** = Area
- **m** = Slope (coefficient)
- **c** = Intercept

---

### Multiple Linear Regression

A Multiple Linear Regression model is trained using all available features to predict house prices.

**Formula:**

\[
y = b_0 + b_1x_1 + b_2x_2 + b_3x_3 + \cdots + b_nx_n
\]

Where:

- **y** = Predicted house price
- **b₀** = Intercept
- **b₁...bₙ** = Feature coefficients
- **x₁...xₙ** = Input features

---

## 6. Prediction

Use the trained regression model to predict house prices for the testing dataset.

---

## 7. Model Evaluation

The model is evaluated using the following metrics:

### Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted values.

**Formula**

\[
MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y_i}|
\]

Lower MAE indicates better model performance.

---

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values.

**Formula**

\[
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y_i})^2
\]

Lower MSE indicates fewer prediction errors.

---

### R² Score (Coefficient of Determination)

Measures how well the regression model explains the variance in the target variable.

**Formula**

\[
R^2 = 1-\frac{\sum(y_i-\hat{y_i})^2}{\sum(y_i-\bar{y})^2}
\]

Where:

- **1** = Perfect prediction
- **0** = Model performs no better than predicting the mean
- Higher values indicate a better model fit.

---

## 8. Visualization

A scatter plot is created for the testing data along with the regression line to visualize the relationship between **Area** and **Price** in Simple Linear Regression.

---

## 9. Interpretation of Coefficients

The regression coefficients indicate the impact of each feature on the predicted house price.

- Positive coefficient → Feature increases house price.
- Negative coefficient → Feature decreases house price.
- Larger magnitude → Greater influence on prediction.

---

## Project Structure

```
Linear_Regression/
│
├── Housing.csv
├── Linear_Regression.ipynb
├── README.md
```

---


## Results

This project successfully demonstrates:

- Data preprocessing
- Simple Linear Regression
- Multiple Linear Regression
- House price prediction
- Model evaluation using MAE, MSE, and R² Score
- Regression line visualization
- Interpretation of regression coefficients

---

## Learning Outcomes

After completing this project, you will understand:

- Fundamentals of Linear Regression
- Difference between Simple and Multiple Linear Regression
- Data preprocessing techniques
- Train-test splitting
- Building regression models using Scikit-learn
- Performance evaluation using MAE, MSE, and R² Score
- Visualization of regression results
- Interpretation of regression coefficients
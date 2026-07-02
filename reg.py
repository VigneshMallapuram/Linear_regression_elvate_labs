import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
df=pd.read_csv('Housing.csv')
print(df.head())
print(df.info())

# Convert Yes/No columns into 1 and 0
binary_columns = [
    'mainroad',
    'guestroom',
    'basement',
    'hotwaterheating',
    'airconditioning',
    'prefarea'
]

for col in binary_columns:
    df[col] = df[col].map({'yes':1, 'no':0})

df = pd.get_dummies(df, columns=['furnishingstatus'], drop_first=True)

print(df.head())

# Independent Variable
X = df[['area']]

# Dependent Variable
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

plt.figure(figsize=(8,6))

plt.scatter(X_test, y_test, color='blue', label="Actual Data")

plt.plot(X_test, y_pred, color='red', linewidth=2, label="Regression Line")

plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Simple Linear Regression")

plt.legend()
plt.show()

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

X = df.drop("price", axis=1)

y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE :", mae)
print("MSE :", mse)
print("R² Score :", r2)

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print(coefficients)
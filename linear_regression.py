
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load the dataset
data = pd.read_csv('/content/Linear_Regression_Testing_Data.csv')
print(data.head())

# Step 2: Separate features (X) and target (y)
X = data[['experience']]   # 2D array
y = data['salary']         # 1D array

# Step 3: Create the model
model = LinearRegression()

# Step 4: Train the model
model.fit(X, y)

# Step 5: Get model parameters
print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)

# Step 6: Predict for training data
y_pred = model.predict(X)

# Step 7: Plot actual vs predicted
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Predicted Line')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression - Actual vs Predicted")
plt.legend()
plt.grid(True)
plt.show()

# Step 8: Evaluate the model
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print("Mean Squared Error:", mse)
print("R² Score:", r2)

# Step 9: Predict for new value (e.g., 12 years)
new_pred = model.predict([[12]])
print("Predicted salary for 12 years of experience:", new_pred[0])

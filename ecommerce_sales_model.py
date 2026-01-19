# ecommerce_sales_model.py

import numpy as np
import pandas as pd
import pickle
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

# Load dataset
esp = pd.read_csv("Ecommerce_Sales_Prediction_Dataset.csv")

# Convert Date to datetime and extract features
esp['Date'] = pd.to_datetime(esp['Date'], dayfirst=True)
esp['day'] = esp['Date'].dt.day
esp['month'] = esp['Date'].dt.month
esp['year'] = esp['Date'].dt.year
esp.drop('Date', axis=1, inplace=True)

# Features and target
X = esp.drop('Units_Sold', axis=1)
y = esp['Units_Sold']

# Preprocessing: one-hot encoding for categorical, scaling for numeric
column_trans = make_column_transformer(
    (OneHotEncoder(sparse_output=False, handle_unknown='ignore'), ['Product_Category', 'Customer_Segment']),
    (StandardScaler(), ['Price', 'Discount', 'Marketing_Spend', 'day', 'month', 'year']),
    remainder='drop'
)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create pipeline with preprocessing + linear regression
pipeline = Pipeline([
    ('preprocessor', column_trans),
    ('regressor', LinearRegression())
])

# Train the model
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")

# Save the trained model to a pickle file
with open("sales_prediction_model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("Model saved as sales_prediction_model.pkl")

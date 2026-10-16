import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from xgboost import XGBRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Load processed dataset
df = pd.read_csv('data/processed_data.csv')

# Features and target
X = df.drop('price', axis=1)

y = df['price']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# Model
model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)

rmse = np.sqrt(mean_squared_error(y_test, predictions))

r2 = r2_score(y_test, predictions)

# Results
print("\nModel Performance")
print("-" * 35)

print(f"MAE Score  : {round(mae, 2)}")

print(f"RMSE Score : {round(rmse, 2)}")

print(f"R2 Score   : {round(r2, 4)}")

print(f"\nModel Accuracy : {round(r2 * 100, 2)}%")

# Feature Importance Graph
importance = model.feature_importances_

features = X.columns

plt.figure(figsize=(10, 6))

plt.barh(features, importance)

plt.title("Feature Importance")

plt.xlabel("Importance Score")

plt.ylabel("Features")

plt.show()

# Save model
joblib.dump(model, 'model.pkl')

# Save scaler
joblib.dump(scaler, 'scaler.pkl')

print("\nModel and scaler saved successfully")
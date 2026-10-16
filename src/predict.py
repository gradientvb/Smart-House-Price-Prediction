import pandas as pd
import joblib

# Load model and scaler
model = joblib.load('model.pkl')

scaler = joblib.load('scaler.pkl')

# Sample house data
sample_data = {
    'bedrooms': [3],
    'bathrooms': [2],
    'sqft_living': [1800],
    'floors': [2],
    'waterfront': [0],
    'condition': [3],
    'grade': [7],
    'yr_built': [2005]
}

# Convert to DataFrame
input_data = pd.DataFrame(sample_data)

# Scale data
scaled_data = scaler.transform(input_data)

# Predict price
prediction = model.predict(scaled_data)

# Convert USD to INR
inr_price = prediction[0] * 83

print("\nPredicted House Price")

print(f"₹ {round(inr_price, 2)}")
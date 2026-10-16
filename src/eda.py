import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('data/kc_house_data.csv')

# Keep important features only
df = df[
    [
        'bedrooms',
        'bathrooms',
        'sqft_living',
        'floors',
        'waterfront',
        'condition',
        'grade',
        'yr_built',
        'price'
    ]
]

# Dataset info
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Price distribution
plt.figure(figsize=(10, 5))

sns.histplot(x=df['price'], kde=True)

plt.title("Price Distribution")

plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))

correlation = df.corr(numeric_only=True)

sns.heatmap(correlation, annot=True, cmap='coolwarm')

plt.title("Correlation Heatmap")

plt.show()

# Save processed dataset
df.to_csv('data/processed_data.csv', index=False)

print("\nProcessed dataset saved successfully")
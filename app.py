from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load('model.pkl')

scaler = joblib.load('scaler.pkl')

print("\n========================================")
print(" Smart House Price Prediction v2 Running")
print(" Open: http://127.0.0.1:5000")
print("========================================\n")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    try:

        bedrooms = float(request.form['bedrooms'])

        bathrooms = float(request.form['bathrooms'])

        sqft_living = float(request.form['sqft_living'])

        floors = float(request.form['floors'])

        waterfront = int(request.form['waterfront'])

        condition = int(request.form['condition'])

        grade = int(request.form['grade'])

        yr_built = int(request.form['yr_built'])

        # Create dataframe
        data = pd.DataFrame({
            'bedrooms': [bedrooms],
            'bathrooms': [bathrooms],
            'sqft_living': [sqft_living],
            'floors': [floors],
            'waterfront': [waterfront],
            'condition': [condition],
            'grade': [grade],
            'yr_built': [yr_built]
        })

        # Scale data
        scaled_data = scaler.transform(data)

        # Predict
        prediction = model.predict(scaled_data)

        result = prediction[0]

        # USD to INR
        inr_price = result * 83

        # Insights
        insight = ""

        if grade >= 9:
            insight = "Luxury Grade House"

        elif sqft_living >= 2500:
            insight = "Spacious Premium Property"

        elif yr_built >= 2015:
            insight = "Modern Recently Built House"

        else:
            insight = "Standard Residential Property"

        return render_template(
            'index.html',
            prediction_text=f'Predicted Price: ₹ {round(inr_price, 2)}',
            insight=insight
        )

    except Exception as e:

        return render_template(
            'index.html',
            prediction_text="Invalid Input"
        )


if __name__ == '__main__':
    app.run(debug=True)
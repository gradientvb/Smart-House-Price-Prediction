# Smart House Price Prediction v2

An end-to-end Machine Learning web application that predicts house prices using advanced regression models and a modern Flask-based user interface.

---

# Features

- Real-time house price prediction
- Machine Learning model using XGBoost
- INR price conversion
- Modern responsive UI
- Feature selection and preprocessing
- Feature importance visualization
- Flask web application
- Clean project structure

---

# Technologies Used

## Backend
- Python
- Flask

## Machine Learning
- Scikit-learn
- XGBoost
- Pandas
- NumPy

## Visualization
- Matplotlib
- Seaborn

## Frontend
- HTML
- CSS

---

# Project Structure

Smart-House-Price-Prediction-v2/

│

├── app.py

├── model.pkl

├── scaler.pkl

├── requirements.txt

├── README.md

│

├── data/

│   ├── kc_house_data.csv

│   └── processed_data.csv

│

├── src/

│   ├── eda.py

│   ├── train.py

│   └── predict.py

│

├── templates/

│   └── index.html

│

├── static/

│

└── screenshots/

---

# Machine Learning Workflow

1. Data Collection
2. Exploratory Data Analysis (EDA)
3. Feature Selection
4. Data Preprocessing
5. Model Training
6. Model Evaluation
7. Flask Integration
8. Deployment Ready System

---

# Selected Features

- bedrooms
- bathrooms
- sqft_living
- floors
- waterfront
- condition
- grade
- yr_built

---

# Model Used

## XGBoost Regressor

Why XGBoost?
- High accuracy
- Handles complex relationships
- Industry-level boosting algorithm
- Better than traditional regression models

---

# Installation

## Clone Repository

```bash
git clone <your-repository-link>
Open Project
cd Smart-House-Price-Prediction-v2

 // Create Virtual Environment :
python -m venv venv

 // Activate Environment
Windows
venv\Scripts\activate 

 // Install Dependencies : 
pip install -r requirements.txt
Run Application
python app.py

 // Open browser:
http://127.0.0.1:5000

// Future Scope
 -> SHAP Explainability
-> Deployment on Render
-> Advanced Dashboard
-> Real Estate Analytics
-> User Authentication
-> Prediction History
-> Cloud Deployment
-> AI Recommendation System

Screenshots
Add screenshots inside:
screenshots/

 // Author : 
Name - Vaibhav
B.Tech CSE (Data Science)
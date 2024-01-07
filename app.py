import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.run(debug=True)
model_path = "C:\\Users\\medis\\OneDrive\\Documents\\j\\github_projects\\jay_loan_app\\Loan_status_prediction\\Training\\loan_model.pkl"
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('loanstatus.html')  # Updated template path

@app.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) if x.strip() else 0.0 for x in request.form.values()]  # Check for non-empty values
    features_value = [np.array(input_features)]

    features_name = ['Current Loan Amount', 'Term', 'Credit Score', 'Annual Income',
                     'Years in current job', 'Home Ownership', 'Years of Credit History',
                     'Number of Credit Problems', 'Bankruptcies', 'Tax Liens',
                     'Credit Problems', 'Credit Age']

    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)
    if output == 1:
        return render_template('fullypaid.html')
    else:
        return render_template('chargedoff.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)

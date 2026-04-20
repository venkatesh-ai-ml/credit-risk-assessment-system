# app.py

from flask import Flask, render_template, request
import joblib
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("best_model.pkl")


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Safely read inputs
        age = float(request.form.get("age", 0))
        income = float(request.form.get("income", 0))
        loan_amount = float(request.form.get("loan_amount", 0))
        credit_score = float(request.form.get("credit_score", 0))
        months_employed = float(request.form.get("months_employed", 0))
        credit_lines = float(request.form.get("credit_lines", 0))
        interest_rate = float(request.form.get("interest_rate", 0))
        loan_term = float(request.form.get("loan_term", 0))
        dti_ratio = float(request.form.get("dti_ratio", 0))

        data = [[
            age, income, loan_amount, credit_score,
            months_employed, credit_lines,
            interest_rate, loan_term, dti_ratio
        ]]

        prob = model.predict_proba(data)[0][1] if hasattr(model, "predict_proba") else model.predict(data)[0]
        prediction = 1 if prob >= 0.40 else 0

        if prediction == 1:
            result = f"⚠️ High Risk Customer ({round(prob*100,2)}%)"
            result_class = "high-risk"
        else:
            result = f"✅ Low Risk Customer ({round((1-prob)*100,2)}%)"
            result_class = "low-risk"

        return render_template(
            "index.html",
            prediction_text=result,
            result_class=result_class
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}",
            result_class="error"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}",
            result_class="error"
        )


# Run App
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
with open("sales_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        data = {
            "Product_Category": request.form["Product_Category"],
            "Customer_Segment": request.form["Customer_Segment"],
            "Price": float(request.form["Price"]),
            "Discount": float(request.form["Discount"]),
            "Marketing_Spend": float(request.form["Marketing_Spend"]),
            "day": int(request.form["day"]),
            "month": int(request.form["month"]),
            "year": int(request.form["year"])
        }

        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

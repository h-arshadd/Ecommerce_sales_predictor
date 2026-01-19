Flask E-commerce Sales Predictor

A Flask web application that predicts e-commerce product sales using a Linear Regression model trained on historical sales data. Users can input product details, customer segment, price, discount, marketing spend, and date to get predicted units sold.

Features

Predict units sold for products based on:

Product category

Customer segment

Price

Discount

Marketing spend

Date (day, month, year)

Built with Flask and a simple, clean HTML/CSS frontend.

Pretrained Linear Regression model saved using pickle.

Demo Screenshot


(Optional: replace with your actual screenshot URL)

Installation

Clone the repository

git clone https://github.com/yourusername/flask-ecommerce-predictor.git
cd flask-ecommerce-predictor


Create and activate virtual environment (optional but recommended)

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate


Install dependencies

pip install -r requirements.txt

Usage

Run the Flask app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/


Fill in the product details in the form and click Predict Sales to see the predicted units sold.

Project Structure
flask-ecommerce-predictor/
│
├─ app.py                  # Flask app
├─ ecommerce_sales_model.py# Linear Regression training script
├─ sales_prediction_model.pkl # Pretrained model
├─ requirements.txt        # Python dependencies
├─ templates/
│   └─ index.html          # HTML template
└─ static/
    └─ style.css           # CSS styles

Dataset

Dataset used: E-commerce Sales Prediction Dataset on Kaggle

Model is trained on historical sales data extracted from this dataset.

Model Details

Linear Regression implemented with scikit-learn.

Preprocessing:

One-hot encoding for categorical features (Product_Category, Customer_Segment)

Scaling for numerical features (Price, Discount, Marketing_Spend, day, month, year)

Trained model is saved as sales_prediction_model.pkl for use in the Flask app.

Future Improvements

Upgrade to more advanced ML models like Random Forest or XGBoost for better predictions.

Enhance frontend UI/UX with responsive design and modern styling.

Deploy online using Render, Railway, or Heroku for public access.

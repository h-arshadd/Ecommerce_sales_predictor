#E-commerce Sales Predictor Using Flask and Linear Regression

A Python web application that predicts e-commerce product sales based on product details, customer segment, pricing, discount, marketing spend, and date. The predictions are powered by a Linear Regression model trained on historical sales data, and served through a Flask web interface.

Dataset

This project uses the E-commerce Sales Prediction Dataset from Kaggle:
E-commerce Sales Prediction Dataset

It contains the following columns:

Date – date of the sale

Product_Category – category of the product (Electronics, Clothing, Furniture)

Customer_Segment – segment of customer (Consumer, Corporate, Home Office)

Price – price of the product

Discount – discount applied to the product

Marketing_Spend – marketing spend for the product

Units_Sold – number of units sold (target variable)

Features

Predicts units sold for any product based on input features.

Uses Linear Regression from scikit-learn with preprocessing:

One-hot encoding of categorical variables (Product_Category, Customer_Segment)

Scaling of numeric features (Price, Discount, Marketing_Spend, day, month, year)

Flask web app with an interactive form for users to input product details.

Clean and responsive HTML/CSS frontend for user-friendly interaction.

Pretrained model is stored in sales_prediction_model.pkl for quick predictions.

Example Output
Web Interface


Users can select product category, customer segment, enter pricing details, and date to predict sales.

Prediction Result


Predicted units sold displayed instantly after submitting the form.

How to Use

Clone the repository

git clone https://github.com/yourusername/flask-ecommerce-predictor.git
cd flask-ecommerce-predictor


Create and activate a virtual environment (optional but recommended)

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run the Flask app

python app.py


Open your browser and go to:

http://127.0.0.1:5000/


Fill in product details and click Predict Sales to see the predicted units sold.

Project Structure
flask-ecommerce-predictor/
│
├─ app.py                  # Flask app
├─ ecommerce_sales_model.py# Model training script
├─ sales_prediction_model.pkl # Trained Linear Regression model
├─ requirements.txt        # Python dependencies
├─ templates/
│   └─ index.html          # HTML template for Flask
└─ static/
    └─ style.css           # CSS styling

Dependencies

Python 3.x

Flask

pandas

numpy

scikit-learn

(All dependencies are listed in requirements.txt)

Future Improvements

Upgrade to advanced ML models like Random Forest or XGBoost for better predictions.

Enhance frontend design and responsiveness.

Deploy online using Render, Railway, or Heroku for public access.

Add more features like seasonal trends, promotions, or user behavior for improved accuracy.

License

This project is open-source and available under the MIT License.

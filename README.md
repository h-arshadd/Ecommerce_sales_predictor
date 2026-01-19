# 🛒 E-commerce Sales Predictor

A **Flask web application** that predicts e-commerce product sales using a **Linear Regression model** trained on historical sales data. Users can input product details, customer segment, price, discount, marketing spend, and date to get predicted units sold.

---

## 📊 Dataset

This project uses the **E-commerce Sales Prediction Dataset** from Kaggle:  
[E-commerce Sales Prediction Dataset](https://www.kaggle.com/datasets/nevildhinoja/e-commerce-sales-prediction-dataset)

**Columns include:**

- `Date` – Date of sale  
- `Product_Category` – Electronics, Clothing, Furniture  
- `Customer_Segment` – Consumer, Corporate, Home Office  
- `Price` – Product price  
- `Discount` – Discount applied  
- `Marketing_Spend` – Marketing spend for the product  
- `Units_Sold` – Target variable (units sold)  

---

## ⚙️ Features

- Predict **units sold** for any product based on input features.  
- Uses **Linear Regression** with preprocessing:  
  - One-hot encoding for categorical features  
  - Scaling for numeric features (`Price`, `Discount`, `Marketing_Spend`, `day`, `month`, `year`)  
- **Interactive Flask web app** with a clean HTML/CSS frontend.  
- Pretrained model stored in **`sales_prediction_model.pkl`**.  

---

## 🖥️ Example Output

### Web Form
![Web Form](screenshots/web_form.png)  
*Users select product category, customer segment, enter price/discount/marketing spend and date.*

### Prediction Result
![Prediction Result](screenshots/prediction_output.png)  
*Predicted units sold displayed after submitting the form.*

---

## 🚀 How to Use

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/flask-ecommerce-predictor.git
cd flask-ecommerce-predictor

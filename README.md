
# 🍽️ Restaurant Sales Prediction

## 📌 Project Overview

Restaurant Sales Prediction is a Machine Learning based project designed to predict the daily sales of a restaurant using historical sales data and other important factors.

The project analyzes different parameters such as:
- Day of the Week
- Month
- Weekend
- Holiday
- Weather Conditions
- Previous Day Sales

Using these factors, the machine learning model predicts expected restaurant sales.

The main objective of this project is to help restaurant owners understand sales patterns, estimate future sales, and make better business decisions.

---

## 🎯 Objectives

1. To analyze historical restaurant sales data.
2. To understand the relationship between sales and different factors.
3. To predict daily restaurant sales using Machine Learning.
4. To display sales information through an interactive dashboard.
5. To help restaurant owners with planning and decision-making.

---

## ✨ Features

- 📊 Total Sales Analysis
- 💰 Average Daily Sales
- 🏆 Best Sales Day
- 📅 Date-Based Sales Prediction
- 🌤️ Weather-Based Sales Analysis
- 🎉 Holiday and Weekend Analysis
- 🤖 Machine Learning Prediction
- 📈 Model Performance Evaluation
- 🖥️ Interactive Streamlit Dashboard

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main Programming Language |
| Pandas | Data Handling and Analysis |
| NumPy | Numerical Operations |
| Scikit-learn | Machine Learning Model |
| Linear Regression | Sales Prediction |
| Matplotlib | Data Visualization |
| Streamlit | Interactive Web Dashboard |

---

## 🤖 Machine Learning Algorithm

### Linear Regression

This project uses the Linear Regression algorithm to predict restaurant sales.

Linear Regression is a supervised machine learning algorithm used to predict numerical values based on input features.

The model learns patterns from historical sales data and uses those patterns to estimate future sales.

### Input Features

- DayOfWeek
- Month
- IsWeekend
- IsHoliday
- PreviousSales
- Weather_Sunny
- Weather_Cloudy
- Weather_Rainy

### Target Variable

- Sales

---

## ⚙️ Project Workflow

1. Collect restaurant sales data.
2. Load the dataset using Pandas.
3. Clean and preprocess the data.
4. Convert weather conditions into numerical features.
5. Select input features and target variable.
6. Split the dataset into training and testing data.
7. Train the Linear Regression model.
8. Evaluate model performance.
9. Display results using Streamlit.
10. Predict sales based on user input.

---

## 📂 Project Structure

```text
Restaurant_Sales_Prediction/
│
├── app.py
│
├── data/
│   └── restaurant_sales.csv
│
├── README.md
│
└── requirements.txt
```

---

## 💻 Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/niteshyadav70447-debug/Restaurant-Sales-Prediction.git
```

### Step 2: Open Project Folder

```bash
cd Restaurant-Sales-Prediction
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

### Step 5: Open in Browser

After running the command, Streamlit will provide a local URL.

Open the following address in your browser:

```text
http://localhost:8501
```

---

## 📊 Model Performance

The Linear Regression model is evaluated using the following metrics:

| Evaluation Metric | Result |
|---|---:|
| MAE | ₹371.20 |
| RMSE | ₹464.22 |
| R² Score | 0.798 |

### Explanation

**1. MAE (Mean Absolute Error)**

MAE measures the average absolute difference between actual sales and predicted sales.

Result: ₹371.20

**2. RMSE (Root Mean Squared Error)**

RMSE measures prediction errors and gives more importance to larger errors.

Result: ₹464.22

**3. R² Score**

R² measures how much variation in sales is explained by the model.

Result: 0.798 or approximately 79.8%.

*Note: These are the results from the project's current practice dataset and model.*

---

## 📈 Dashboard Information

The Streamlit dashboard provides the following information:

- Total Restaurant Sales
- Average Daily Sales
- Best Sales Day
- Sales Prediction
- Weather Selection
- Holiday Selection
- Previous Day Sales Input
- Model Evaluation Metrics

Users can enter different values and view the predicted sales.

---

## 🚀 Applications

This project can be useful for:

- Restaurant Owners
- Restaurant Managers
- Sales Planning
- Inventory Management
- Demand Forecasting
- Business Decision-Making

---

## 🔮 Future Improvements

In the future, this project can be improved by:

1. Using larger real-world restaurant datasets.
2. Adding more machine learning algorithms.
3. Implementing advanced forecasting models.
4. Adding monthly and yearly sales predictions.
5. Integrating real-time weather information.
6. Improving dashboard design.
7. Deploying the application online.

---

## ⚠️ Disclaimer

This project is developed for educational and learning purposes.

The dataset used is a practice dataset. Predictions are estimates and should not be treated as guaranteed future sales.

---

## 👨‍💻 Developer

**Project Name:** Restaurant Sales Prediction

**Developed By:** Nitesh Yadav

**GitHub Repository:**

https://github.com/niteshyadav70447-debug/Restaurant-Sales-Prediction

---

## ⭐ Conclusion

The Restaurant Sales Prediction project demonstrates how Machine Learning can be used to analyze historical restaurant sales and predict future sales.

By using Python, Linear Regression, and Streamlit, this project provides an interactive way to understand sales trends and support better business planning.

**Thank You!**


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

st.set_page_config(
    page_title="Restaurant Sales Prediction",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Restaurant Sales Prediction")
st.write("Predict daily restaurant sales using demand-related factors.")

@st.cache_data
def load_data():
    df = pd.read_csv("data/restaurant_sales.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

df["Weather"] = df["Weather"].astype(str)
data = pd.get_dummies(df, columns=["Weather"], dtype=int)

features = [
    "DayOfWeek",
    "Month",
    "IsWeekend",
    "IsHoliday",
    "PreviousSales",
    "Weather_Sunny",
    "Weather_Cloudy",
    "Weather_Rainy"
]

X = data[features]
y = data["Sales"]

split = int(len(data) * 0.8)

X_train = X.iloc[:split]
X_test = X.iloc[split:]
y_train = y.iloc[:split]
y_test = y.iloc[split:]

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

st.subheader("📊 Historical Sales Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sales",
    f"₹{df['Sales'].sum():,.0f}"
)

col2.metric(
    "Average Daily Sales",
    f"₹{df['Sales'].mean():,.0f}"
)

col3.metric(
    "Best Sales Day",
    f"₹{df['Sales'].max():,.0f}"
)

st.subheader("📈 Daily Sales Trend")

fig, ax = plt.subplots(figsize=(12, 4))

ax.plot(
    df["Date"],
    df["Sales"],
    label="Daily Sales"
)

ax.set_xlabel("Date")
ax.set_ylabel("Sales (₹)")
ax.legend()
ax.grid(alpha=0.3)

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.subheader("📉 Actual vs Predicted Sales")

comparison = pd.DataFrame({
    "Actual Sales": y_test.values,
    "Predicted Sales": predictions
})

st.line_chart(comparison)

st.subheader("🤖 Predict Restaurant Sales")

with st.form("prediction_form"):

    date_input = st.date_input(
        "Select Prediction Date"
    )

    weather = st.selectbox(
        "Select Weather",
        ["Sunny", "Cloudy", "Rainy"]
    )

    holiday = st.selectbox(
        "Is it a Holiday?",
        ["No", "Yes"]
    )

    previous_sales = st.number_input(
        "Previous Day Sales (₹)",
        min_value=0.0,
        value=8000.0,
        step=500.0
    )

    submitted = st.form_submit_button(
        "Predict Sales"
    )

if submitted:

    date = pd.Timestamp(date_input)

    new_data = pd.DataFrame([{
        "DayOfWeek": date.dayofweek,
        "Month": date.month,
        "IsWeekend": int(date.dayofweek >= 5),
        "IsHoliday": int(holiday == "Yes"),
        "PreviousSales": previous_sales,
        "Weather_Sunny": int(weather == "Sunny"),
        "Weather_Cloudy": int(weather == "Cloudy"),
        "Weather_Rainy": int(weather == "Rainy")
    }])

    predicted_sales = model.predict(
        new_data[features]
    )[0]

    predicted_sales = max(0, predicted_sales)

    st.success(
        f"Predicted Daily Sales: ₹{predicted_sales:,.2f}"
    )

st.subheader("📋 Model Performance")

col1, col2, col3 = st.columns(3)

col1.metric("MAE", f"₹{mae:,.2f}")
col2.metric("RMSE", f"₹{rmse:,.2f}")
col3.metric("R² Score", f"{r2:.3f}")

st.caption(
    "Note: This project uses a synthetic practice dataset. "
    "Predictions are illustrative, not real restaurant forecasts."
)

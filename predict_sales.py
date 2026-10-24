
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("data/restaurant_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Prepare weather columns
df = pd.get_dummies(df, columns=["Weather"], dtype=int)

features = [
    "DayOfWeek", "Month", "IsWeekend", "IsHoliday",
    "PreviousSales", "Weather_Sunny",
    "Weather_Cloudy", "Weather_Rainy"
]

X = df[features]
y = df["Sales"]

# Train model
# Train model
model = LinearRegression()
model.fit(X, y)

model.fit(X, y)

print("\nRESTAURANT SALES PREDICTION")
print("-" * 35)

date_input = input("Enter prediction date (YYYY-MM-DD): ")
weather = input("Weather (Sunny/Cloudy/Rainy): ").strip().title()
holiday = int(input("Is it a holiday? (1=Yes, 0=No): "))
previous_sales = float(input("Previous day's sales (Rs): "))

date = pd.to_datetime(date_input)

if weather not in ["Sunny", "Cloudy", "Rainy"]:
    raise ValueError("Weather must be Sunny, Cloudy, or Rainy.")

if holiday not in [0, 1]:
    raise ValueError("Holiday must be 1 or 0.")

if previous_sales < 0:
    raise ValueError("Previous sales cannot be negative.")

day = date.dayofweek
month = date.month
weekend = int(day >= 5)

new_data = pd.DataFrame([{
    "DayOfWeek": day,
    "Month": month,
    "IsWeekend": weekend,
    "IsHoliday": holiday,
    "PreviousSales": previous_sales,
    "Weather_Sunny": int(weather == "Sunny"),
    "Weather_Cloudy": int(weather == "Cloudy"),
    "Weather_Rainy": int(weather == "Rainy")
}])

prediction = model.predict(new_data[features])[0]
prediction = max(0, prediction)

print("\nPrediction Result")
print("-" * 35)
print("Date:", date.strftime("%d-%m-%Y"))
print("Day:", date.day_name())
print("Weather:", weather)
print("Predicted Sales: Rs.", round(prediction, 2))

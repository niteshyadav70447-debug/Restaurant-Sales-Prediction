
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor

# Load dataset
df = pd.read_csv("data/restaurant_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Convert weather into numeric columns
df = pd.get_dummies(df, columns=["Weather"], dtype=int)

# Select features and target
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

X = df[features]
y = df["Sales"]

# Split data chronologically
split = int(len(df) * 0.8)

X_train = X.iloc[:split]
X_test = X.iloc[split:]

y_train = y.iloc[:split]
y_test = y.iloc[split:]

# Train Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

# Train XGBoost
xgb_model = XGBRegressor(
    n_estimators=200,
    max_depth=3,
    learning_rate=0.05,
    objective="reg:squarederror",
    random_state=42
)

xgb_model.fit(X_train, y_train)
xgb_predictions = xgb_model.predict(X_test)

# Evaluate models
def evaluate_model(name, actual, predicted):
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    r2 = r2_score(actual, predicted)

    print(f"\n{name}")
    print(f"MAE: ₹{mae:.2f}")
    print(f"RMSE: ₹{rmse:.2f}")
    print(f"R2 Score: {r2:.3f}")

evaluate_model("Linear Regression", y_test, lr_predictions)
evaluate_model("XGBoost", y_test, xgb_predictions)

# Plot actual vs predicted sales
plt.figure(figsize=(12, 6))
plt.plot(df["Date"].iloc[split:], y_test.values, label="Actual Sales")
plt.plot(df["Date"].iloc[split:], xgb_predictions, label="XGBoost Predictions")

plt.title("Restaurant Sales: Actual vs Predicted")
plt.xlabel("Date")
plt.ylabel("Sales (₹)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_prediction.png")
plt.show()

print("\nGraph saved as sales_prediction.png")


import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2025-01-01", periods=365, freq="D")

df = pd.DataFrame({
    "Date": dates
})

df["DayOfWeek"] = df["Date"].dt.dayofweek
df["Month"] = df["Date"].dt.month
df["IsWeekend"] = (df["DayOfWeek"] >= 5).astype(int)
df["IsHoliday"] = np.random.choice([0, 1], size=365, p=[0.92, 0.08])
df["Weather"] = np.random.choice(
    ["Sunny", "Cloudy", "Rainy"], size=365, p=[0.5, 0.3, 0.2]
)

weather_effect = df["Weather"].map({
    "Sunny": 500,
    "Cloudy": 200,
    "Rainy": -400
})

weekend_effect = df["IsWeekend"] * 1500
holiday_effect = df["IsHoliday"] * 2000
trend = np.arange(365) * 3
noise = np.random.normal(0, 500, 365)

df["Sales"] = (
    5000 + weekend_effect + holiday_effect
    + weather_effect + trend + noise
).round().astype(int)

df["PreviousSales"] = df["Sales"].shift(1)
df = df.dropna().reset_index(drop=True)
df["PreviousSales"] = df["PreviousSales"].astype(int)

df.to_csv("data/restaurant_sales.csv", index=False)

print("Dataset created successfully!")
print(df.head())
print("Dataset shape:", df.shape)

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima
from scipy.optimize import minimiz

# Define the tickers and date range
tickers = ["TSLA", "BND", "SPY"]
start_date = "2015-01-01"
end_date = "2025-01-31"

# Fetch the data
df = yf.download(tickers, start=start_date, end=end_date)

# Select only closing prices
closing_prices = df["Close"]

# Train-Test Split
train_size = int(len(df) * 0.8)
train, test = df[:train_size], df[train_size:]

# ARIMA Model for Forecasting
# Auto-select ARIMA parameters
arima_model = auto_arima(train['TSLA'], seasonal=False, trace=True)

# Train ARIMA
model = ARIMA(train['TSLA'], order=arima_model.order)
model_fit = model.fit()

# Forecast
forecast = model_fit.forecast(steps=len(test))

# Plot forecast vs actual
plt.figure(figsize=(12, 6))
plt.plot(test.index, test['TSLA'], label='Actual TSLA')
plt.plot(test.index, forecast, label='Forecast TSLA', linestyle='dashed')
plt.legend()
plt.title("TSLA Stock Price Forecast (ARIMA)")
plt.show()

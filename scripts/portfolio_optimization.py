import pandas as pd
import numpy as np
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA

# Define the tickers and date range
tickers = ["TSLA", "BND", "SPY"]
start_date = "2015-01-01"
end_date = "2025-01-31"

# Fetch the data
df = yf.download(tickers, start=start_date, end=end_date)

#Forecast Future Prices for TSLA, BND, and SPY
future_steps = 365  # 1 year ahead
forecasted_prices = {}

for tickers in df.columns:
    model = ARIMA(df[tickers], order=(1,1,1))
    model_fit = model.fit()
    forecasted_prices[tickers] = model_fit.forecast(steps=future_steps)

# Convert forecasts to DataFrame
forecast_df = pd.DataFrame(forecasted_prices, index=pd.date_range(start=df.index[-1], periods=future_steps))

import pandas as pd
import numpy as np
import yfinance as yf
from scipy.optimize import minimize
# Define the tickers and date range
tickers = ["TSLA", "BND", "SPY"]
start_date = "2015-01-01"
end_date = "2025-01-31"

# Fetch the data
df = yf.download(tickers, start=start_date, end=end_date)

# Compute daily returns
returns = df.pct_change().dropna()

# Define function to calculate Sharpe Ratio
def sharpe_ratio(weights):
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    return - (portfolio_return / portfolio_volatility)  # Negative for minimization

# Initial weights
initial_weights = np.array([0.33, 0.33, 0.34])  

# Constraints: Sum of weights must be 1
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# Bounds for each weight (0 to 1)
bounds = [(0, 1) for _ in range(len(df.columns))]

# Optimize portfolio weights
optimized_result = minimize(sharpe_ratio, initial_weights, bounds=bounds, constraints=constraints)

# Get optimized weights
optimized_weights = optimized_result.x

# Print results
print(f"Optimized Portfolio Weights:\nTSLA: {optimized_weights[0]:.2f}, BND: {optimized_weights[1]:.2f}, SPY: {optimized_weights[2]:.2f}")

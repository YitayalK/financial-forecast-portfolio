# Financial Forecasting Portfolio

## Overview
This project focuses on financial data analysis and forecasting using historical stock market data. The goal is to explore market trends, perform statistical analysis, and develop predictive models for investment decision-making.

## Task 1: Exploratory Data Analysis (EDA)
Exploratory Data Analysis was conducted to understand the structure, trends, and patterns in the dataset. The main steps included:

- **Data Collection:** Historical stock prices were fetched using the Yahoo Finance API (`yfinance`).
- **Data Cleaning:** Ensured proper formatting, checked for missing values, and handled any inconsistencies.
- **Statistical Summary:** Computed key statistical metrics (mean, standard deviation, min, max, etc.).
- **Visualization:** Used Matplotlib and Seaborn to create various plots:
  - Line charts for closing prices.
  - Histogram distributions.
  - Moving averages for trend analysis.

## Installation
To set up the environment, install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the following script to fetch and analyze the data:
```bash
python eda.py
```

## Directory Structure
```
financial-forecasting-portfolio/
│-- data/
│   ├── historical_data.csv
│-- notebooks/
│   ├── exploratory_data_analysis.ipynb
│-- scripts/
│   ├── fetch_data.py
│   ├── eda.py
│-- README.md
│-- requirements.txt
```

## Dependencies
- Python 3.8+
- Pandas
- NumPy
- Matplotlib
- Seaborn
- yfinance

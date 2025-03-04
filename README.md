# Financial Forecasting Portfolio

## Project Overview
This project aims to forecast financial market trends using machine learning models. It involves data collection, exploratory data analysis (EDA), time series forecasting with ARIMA, and model evaluation. The project follows a structured approach, including data preprocessing, model training, and deployment.

## Tasks

### Task 1: Data Collection
- **Objective:** Gather historical financial data for analysis.
- **Sources:** Yahoo Finance API.
- **Process:**
  - Fetch stock price data.
  - Handle missing values and anomalies.

### Task 2: Exploratory Data Analysis (EDA)
- **Objective:** Understand the dataset structure and trends.
- **Key Steps:**
  - Visualize time series data.
  - Identify patterns and seasonality.
  - Compute statistical summaries.
  - Handle missing values.

### Task 3: Time Series Forecasting with ARIMA
- **Objective:** Train ARIMA models for financial time series prediction.
- **Process:**
  - Select optimal ARIMA parameters using `pmdarima.auto_arima`.
  - Train ARIMA model.
  - Evaluate model performance using metrics like RMSE and MAPE.
  - Plot actual vs. predicted values.

### Task 4: Model Evaluation and Optimization
- **Objective:** Assess model performance and optimize hyperparameters.
- **Approach:**
  - Compare ARIMA with alternative models (e.g., SARIMA, LSTMs).
  - Perform cross-validation.
  - Fine-tune parameters for better accuracy.

## Installation & Setup

### Prerequisites
Ensure you have Python installed (recommended version: 3.9+). Install dependencies using:
```sh
pip install -r requirements.txt
```

### Running the Project
1. **Activate Virtual Environment:**
   ```sh
   source ffpvenv/bin/activate  # On macOS/Linux
   ffpvenv\Scripts\activate  # On Windows
   ```
2. **Run Data Collection:**
   ```sh
   python scripts/data_collection.py
   ```
3. **Perform EDA:**
   ```sh
   python scripts/eda.py
   ```
4. **Train ARIMA Model:**
   ```sh
   python scripts/model_training.py
   ```

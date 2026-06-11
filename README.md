# Bitcoin-Price-Predictor


## Overview

Bitcoin Price Predictor is a machine learning-based forecasting system developed to analyze historical Bitcoin market data and predict future price trends. The project utilizes time-series forecasting techniques and machine learning models to study Bitcoin price movements using historical Open, High, Low, Close, and Volume (OHLCV) data.

The system collects historical cryptocurrency data, performs preprocessing and feature engineering, and applies multiple predictive models including Auto Regression (AR), Auto Regressive Moving Average (ARMA), Auto Regressive Integrated Moving Average (ARIMA), and Support Vector Machine (SVM) models. The performance of each model is evaluated using prediction accuracy and Root Mean Square Error (RMSE).

---

## Features

* Historical Bitcoin data collection using CoinMarketCap API
* Data preprocessing and normalization
* Feature engineering using OHLCV market indicators
* Time-series forecasting using AR, ARMA, and ARIMA models
* Machine learning-based prediction using Support Vector Machine (SVM)
* Model evaluation using RMSE
* Visualization of actual vs predicted Bitcoin prices
* Comparative analysis of forecasting techniques

---

## Dataset

The dataset consists of historical Bitcoin market information including:

* Open Price
* High Price
* Low Price
* Close Price
* Trading Volume
* Daily Mean Price

Data is collected from the CoinMarketCap historical cryptocurrency API.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Statsmodels
* Matplotlib
* Requests
* Jupyter Notebook
  

## Models Implemented

### AR (Auto Regression)

Forecasts future Bitcoin prices using previous observations.

### ARMA (Auto Regressive Moving Average)

Combines autoregressive and moving average components for prediction.

### ARIMA (Auto Regressive Integrated Moving Average)

Handles non-stationary time-series data through differencing and forecasting.

### SVM (Support Vector Machine)

Machine learning model used to predict Bitcoin price trends based on historical market features.

---

## Results

The implemented models generate future Bitcoin price predictions and visualize actual versus predicted values. Model performance is evaluated using RMSE to compare forecasting accuracy.

---

## Future Improvements

* Integration of LSTM and GRU deep learning models
* Real-time cryptocurrency price prediction
* Sentiment analysis using social media and news data
* Interactive web dashboard for live forecasting
* Multi-cryptocurrency prediction support

---


---

## License

This project is developed for academic and research purposes.

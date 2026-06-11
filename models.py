from statsmodels.tsa.ar_model import AR

model = AR(train_y)
results = model.fit()
predictions = results.predict(...)



from statsmodels.tsa.arima_model import ARMA

model = ARMA(
    train_y,
    exog=train_X,
    order=(0,1,1)
)



from statsmodels.tsa.arima_model import ARIMA

model = ARIMA(
    train_y,
    exog=train_X,
    order=(0,1,1)
)


from sklearn.svm import SVR

model = SVR(
    kernel='rbf',
    C=100,
    gamma=0.1
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

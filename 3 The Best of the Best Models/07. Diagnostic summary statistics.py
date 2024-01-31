#1
# Create and fit model
model1 = ARIMA(df, order=(3, 0, 1))
results1 = model1.fit()

# Print summary
print(results1.summary())

#3
# Create and fit model
model2 = ARIMA(df, order=(2,0,0))
results2 = model2.fit()

# Print summary
print(results2.summary())

# Instantiate the model
model = ARIMA(earthquake, order = (3, 0, 1))

# Fit the model
results = model.fit()

# Print model fit summary
print(results.summary())

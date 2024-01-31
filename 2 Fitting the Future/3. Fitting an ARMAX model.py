# Instantiate the model
model = ARIMA(hospital['wait_times_hrs'], order = (2, 0, 1), exog = hospital['nurse_count'])

# Fit the model
results = model.fit()

# Print model fit summary
print(results.summary())

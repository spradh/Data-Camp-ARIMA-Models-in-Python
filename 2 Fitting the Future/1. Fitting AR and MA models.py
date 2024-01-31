#1
# Instantiate the model
model = ARIMA(sample['timeseries_1'], order=(2, 0, 0))

# Fit the model
results = model.fit()

# Print summary
print(results.summary())


#3
# Instantiate the model
model = ARIMA(sample['timeseries_2'], order=(0, 0, 3))

# Fit the model
results = model.fit()

# Print summary
print(results.summary())

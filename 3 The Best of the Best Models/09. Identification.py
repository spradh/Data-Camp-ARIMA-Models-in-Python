# Plot time series
savings.plot()
plt.show()

# Run Dicky-Fuller test
result = adfuller(savings)

# Print test statistic
print(result[0])

# Print p-value
print(result[1])

# Create and fit model
model = ARIMA(savings, order=(1, 0, 2))
results = model.fit()

# Create the 4 diagostics plots
results.plot_diagnostics()
plt.show()

# Print summary
print(results.summary())

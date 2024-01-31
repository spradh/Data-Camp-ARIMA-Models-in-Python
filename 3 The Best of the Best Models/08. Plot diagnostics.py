# Create and fit model
model = ARIMA(df, order=(1, 1, 1))
results = model.fit()

# Create the 4 diagnostics plots
results.plot_diagnostics()
plt.show()

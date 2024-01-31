# Create figure
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,8))
 
# Plot the ACF of savings on ax1
plot_acf(savings, zero=False, lags=10, ax=ax1)

# Plot the PACF of savings on ax2
plot_pacf(savings, zero=False, lags=10, ax=ax2)


plt.show()

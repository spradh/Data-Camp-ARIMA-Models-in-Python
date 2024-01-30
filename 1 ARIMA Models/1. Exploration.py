# Import modules
import matplotlib.pyplot as plt
import pandas as pd

# Load in the time series
candy = pd.read_csv('candy_production.csv', 
            index_col = 'date',
            parse_dates = True)

# Plot and show the time series on axis ax1
fig, ax1 = plt.subplots()
ax1.plot(ax=____)
____

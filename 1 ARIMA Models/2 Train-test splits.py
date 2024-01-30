# Split the data into a train and test set
candy_train = candy.loc[: '2006-12-31'] #exercise is incorrect - this should be 2001-01-01/ there is a break in the data -> it doesn't matter for this exercise since the data is monthly captured on the 1st of eery month but wouldn't work for daily level data.
candy_test = candy.loc['2007-01-01':]

# Create an axis
fig, ax = plt.subplots()

# Plot the train and test sets on the axis ax
candy_train.plot(ax=ax)
candy_test.plot(ax=ax)
plt.show()

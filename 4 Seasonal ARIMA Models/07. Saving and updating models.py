#1
# Import joblib
import joblib

# Set model name
filename = 'candy_model.pkl'

# Pickle it
joblib.dump(model,filename)

#2
# Import
import joblib

# Set model name
filename = "candy_model.pkl"

# Load the model back in
loaded_model = joblib.load(filename)

#3
# Update the model
loaded_model.update(df_new)

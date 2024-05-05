# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# Load the Iris dataset from sklearn
iris = load_iris()

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])

# Display the first few rows of the dataframe
print("Original Dataset:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for duplicated rows
print("\nDuplicated Rows:")
print(df.duplicated().sum())

# Drop duplicated rows if any
df = df.drop_duplicates()

# Encode categorical target variable (if any)
# In the Iris dataset, the target variable is numerical, so no need for encoding

# Split data into features and target variable
X = df.drop('target', axis=1)
y = df['target']

# Perform any other preprocessing steps as needed, such as scaling, encoding categorical features, etc.

# Finally, you can save the preprocessed data if needed
# For example, to save as a CSV file
df.to_csv('preprocessed_iris.csv', index=False)

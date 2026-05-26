import pandas as pd
print(pd.__version__)

data = {
    "Name": ["Ram", "Sita", "Hari", "Gita", "Raj"],
    "Age": [20, 22, 21, 23, 20],
    "Marks": [75, 88, 45, 92, 61]
}

# Convert data into DataFrame
df = pd.DataFrame(data)
print(df) 
# Prints entire dataframe

print(df.head(3))
# Prints just the first 3 rows

print (df["Marks"])
# Prints the Marks column only

print (df.describe())
# Prints basic statistics of the data

print (df.shape)
# Prints rows and columns

# WHY WE USE DataFrames:
# A regular Python dictionary can store data but has no analysis tools.
# A pandas DataFrame organizes the same data into a table (rows and columns)
# and gives you hundreds of built-in tools for analysis:
# filtering, sorting, statistics, handling missing values, and more.
# In real data science, DataFrames are loaded directly from CSV files.
# Converting a dictionary to a DataFrame: df = pd.DataFrame(data)
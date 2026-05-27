import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
# Dataset downloaded from kaggle

pd.set_option('display.max_columns', None)
# Used to  tell pandas to never truncate columns regardless of screen width

# Print first 5 rows
print(df.head(5))

# Print the shape
print(df.shape)

# Print column names
print(df.columns)

# Print basic statistics
print(df.describe())
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
# Dataset downloaded from kaggle

pd.set_option('display.max_columns', None)
# Used to  tell pandas to never truncate columns regardless of screen width

# Students who score more than 80 in math
print(df[df["math score"] > 80]) 

# Show only female students
print(df[df["gender"] == "female"])

# Name of columns
print(df.columns)

# Student who scored more than 70 in both math and reading
print(df[(df["math score"] > 70) & (df["reading score"] > 70)])

# Count how many students passed math
print(df[df["math score"] > 40].shape[0])  


# PANDAS FILTERING NOTES
# Basic filtering syntax: df[df["column name"] > value]
# Pandas filters the entire DataFrame at once — no loops needed.

# String conditions need quotes: df[df["gender"] == "female"]

# Multiple conditions use & (AND) and | (OR) — not Python's 'and'/'or'
# Reason: pandas handles 1000 rows at once, 'and' only handles one True/False
# Always wrap each condition in parentheses:
# df[(df["math score"] > 70) & (df["reading score"] > 70)]

# .shape returns (rows, columns) as a tuple
# .shape[0] = number of rows
# .shape[1] = number of columns
# Use .shape[0] after filtering to count matching rows
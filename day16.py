import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

pd.set_option("display.max_columns", None)

# GROUPBY:
# groupby splits the DataFrame into groups based on a column
# then lets you apply calculations to each group separately
# syntax: df.groupby("column")["target column"].calculation()

# Average math score grouped by gender
print(df.groupby("gender")["math score"].mean())

# Average of multiple scores grouped by test preparation course
# Multiple columns selected using a list inside brackets
print(df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean())

# NOTES:
# .groupby("column") — splits data by unique values in that column
# ["column name"] — selects which column to calculate on
# [["col1", "col2"]] — double brackets to select multiple columns
# .mean() — calculates average per group
# Other calculations: .sum(), .count(), .min(), .max() all work the same way

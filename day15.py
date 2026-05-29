import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

pd.set_option('display.max_columns', None)

# Create a new column "total score" that adds math, reading, and writing scores together
# Pandas adds entire columns at once — no loops needed
df["total score"] = df["math score"] + df["reading score"] + df["writing score"]
print(df["total score"])

# Create column called "average score" that calculates the average of the three
df["average score"] = df["total score"] / 3
print(df["average score"])

# Create a "result" column that says "Pass" if average score is above 40, "Fail" otherwise

# Normal function approach — readable but longer
def check_result(x):
    if x > 40:
        return "Pass"
    else:
        return "Fail"

df["result"] = df["average score"].apply(check_result)

# Lambda approach — same logic in one line
# lambda x: is a mini throwaway function where x = each individual value in the column
# .apply() loops through every row automatically and applies the function
df["result"] = df["average score"].apply(lambda x: "Pass" if x > 40 else "Fail")

# Print the first 10 rows showing all new columns
print(df.head(10))

# Count how many passed and how many failed
# .shape[0] returns number of rows in the filtered result
print("Passed:", df[df["result"] == "Pass"].shape[0])
print("Failed:", df[df["result"] == "Fail"].shape[0])
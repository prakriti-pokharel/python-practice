my_dict = {"Ram": 60, "Ravi": 70, "Rita": 35}

# Average
total = 0
for key, value in my_dict.items():
    total += value
avg = total / 3
print("Class average:", avg)

# Highest
highest_mark = 0
highest_name = ""
for key, value in my_dict.items():
    if value > highest_mark:
        highest_mark = value
        highest_name = key

print("Highest mark:", highest_mark, "scored by:", highest_name)

# Pass/Fail
for key, value in my_dict.items():
    if value >= 40:
        print(key, "passed, marks:", value)
    else:
        print(key, "failed, marks:", value)
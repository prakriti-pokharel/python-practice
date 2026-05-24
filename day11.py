coordinates = (27.7172, 85.3240)  # Kathmandu latitude/longitude
print(coordinates)
# coordinates[0]= 56.43 causes erroe : Tuple doesn't allow changes

skills = {"python", "sql", "pandas", "python", "sql"}
print(skills) # Duplicates will be removed upon printing
skills.add("numpy")
print(skills)

# Note:List allows duplicates, set does not

# Convert set to list (initial approach)
my_list = []
for x in skills:
    my_list.append(x)

# Better approach
my_list = list(skills) # list() converts (set/ tuple/ dictionary) into a list
print (my_list)

# Sort the list alphabetically
my_list.sort()
print(my_list)
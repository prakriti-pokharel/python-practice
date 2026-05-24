coordinates = (27.7172, 85.3240)  # Kathmandu latitude/longitude
print(coordinates)
#coordinates[0]= 56.43 causes erroe : Tuple doesn't allow changes

skills = {"python", "sql", "pandas", "python", "sql"}
print(skills) #Duplicates will be removed upon printing
skills.add("numpy")
print(skills)

# Note:List allows duplicates, set does not

my_list = []
for x in skills:
    my_list.append(x)
print (my_list)

my_list.sort()
print(my_list)
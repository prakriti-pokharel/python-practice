# Loop through list and print only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in numbers:
    if x%2==0:
        print (x)

# Loop through the same list and build a new list containing only even numbers
newnum =[]
for x in numbers:
    if x%2==0:
        newnum.append(x)
print(newnum)

# Loop through given dictionary and print only students who scored above 50
students = {"Ram": 45, "Sita": 72, "Hari": 38, "Gita": 91, "Raj": 55}
print("Students who scored more than 50:")
for key,value in students.items():
    if value >50:
        print (key)

# Loop through same dictionary and create a new dictionary with only the passing students
newstd ={}
for key,value in students.items():
    if value >50:
        newstd[key] = value
print(newstd)
        
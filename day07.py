#Creating list of 5 student names
my_list = ["Ryan", "Tina", "Kristi", "Boyd", "Jim"]

#Ask user to inout a name
name = input("Enter a name: ")

#Check if name is in the list
if name in my_list:
    print("Name found in the list in position:", my_list.index(name)+1)
else:
    print("Name not found!")
    
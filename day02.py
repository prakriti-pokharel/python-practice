#Creating dictionary with 3 keys
my_dict = {"name":"Prakriti","age":10,"city":"Kathmandu"}

#Printing each key and value using loop (initial approach)
for x in my_dict:
    print(x) #printing key
    print(my_dict[x]) #printing values

#(better approach)
for key, value in my_dict.items(): #Without .items() your loop only sees the keys
    print(key, ":", value)

#Function that takes a name and returns in uppercase
def my_fun(n):
    return n.upper()

#Calling the function (hardcoded name)
print(my_fun("Ram"))

#Fetching name from dictionary
print(my_fun(my_dict["name"]))
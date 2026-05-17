#List
my_list = [71,9,3,5,6,20]

#Function that returns largest number
def largest(lst):
    large = lst[0]
    for x in lst:
        if x > large:
            large =x
    return large

#Function that returns sum
def total(lst):
    s=0
    for x in lst:
        s+=x
    return s

#Calling the functions
print("Largest:", largest(my_list))
print("Sum:", total(my_list))
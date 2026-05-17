#Ask user to enter a number
n= int(input ("Enter a number: "))

#Conditionals
if n> 10:
    print(n,"is greater than 10")
elif n<10:
    print(n,"is not greater than 10")
else:
    print(n,"is equal to 10")

#Function returning even/odd
def odd_even(n):
    if n %2 ==0:
        return str(n) + " is Even"
    else:
        return str(n) + " is Odd"

#Calling the function
print(odd_even(n))
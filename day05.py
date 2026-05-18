#While loop that counts from 1 to 10
i=1
while i<=10:
    print (i)
    i+=1

#While loop to ask user to enter a number until they enter 0 and print how many numbers they entered
count=0
x=int(input("Enter a number: "))
while x!=0:
    count+=1
    x= int(input("Enter another number: "))
print ("Numbers entered: ", count)

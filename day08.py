# Write 5 names to a file
with open("students.txt", "w") as file: # Created a file named "students.txt" and wrote names
    file.write("Ariana Grande\n")
    file.write("Billie Eilish\n")
    file.write("Chris Brown\n")
    file.write("Ellie Goulding\n")
    file.write("Charlie Puth\n")

# First read
with open("students.txt", "r") as file:
    content1 = file.read()
    print(content1)

# Second read
with open("students.txt", "r") as file:
    content2 = file.readlines()
    print (content2)
    for x in content2:
        print(x.strip())

# Notes:
# - You can only read a file once per open
# - readlines() gives you a list where each line is a separate item
# - .strip() removes whitespace from both ends
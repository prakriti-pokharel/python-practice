# Write 5 names to a file
with open("students.txt", "w") as file: # Created a file named "students.txt" and wrote names
    file.write("Ariana Grande\n")
    file.write("Billie Eilish\n")
    file.write("Chris Brown\n")
    file.write("Ellie Goulding\n")
    file.write("Charlie Puth\n")

# Read and print each name
with open("students.txt","r") as file:
    content = file.read()
    print(content)

num = 7
attempt =1 #First guess counts
guess = int(input("Guess the number: "))
while guess!=num:
    if guess>num:
        print("Lower!")
    else:
        print("Higher")
    guess = int(input("Guess again: "))
    attempt+=1
print("You guessed it in", attempt, "attempts!")
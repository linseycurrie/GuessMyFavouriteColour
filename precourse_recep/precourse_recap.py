colour = "Blue"

userGuess = input("Guess my favourite colour : ")

if userGuess.capitalize() == colour:
    print("Well Done! You got it right!")
else:
    print("Opps, sorry it's not " + userGuess)
# Building a secret guessing game

secret_word = "love" #Our secret word to be guessed
guess = "" #This is empty variable to store the user guess
guess_count = 0 #This is responsible for the looping process
guess_limit = 2 #This is the amount of times your guesses are valid
out_of_guesses = False #This woould only be set to true if we have just a single guess limit

while guess != secret_word and not(out_of_guesses): #While our guess is not equals to the secret word and also not out of guesses
    if guess_count < guess_limit: #If guess count is lesser than guess limit
        guess = input("Enter your guess: ")
        guess_count +=  1 #Guess count is added by 1 since it is a loop
    else:
        out_of_guesses = True #If out of guesses which is equal to 2
if out_of_guesses:
        print("Out of guesses, you LOSE!") #You LOSE!
else:
        print("Right guess, you win!") #Congratulations, 2,000 USD awaits you in the bank!
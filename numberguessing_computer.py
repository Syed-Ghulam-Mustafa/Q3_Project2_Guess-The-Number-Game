# Project 2 : Number Guessing Game in Python.
# 1 to 100 numbers
# random ka use is liye kr rhay hain qk computer randomly (1-100) mein se koi number choose karega.
# random librarry h jo built-in hai python mein. aur random numbers etc k liye use hoti hai.
# randint ka use is liye kia hai qk hume random numbers chahiye hain.
# randint ka mtlb hai random integer. aur (1, 100) ka mtlb hai 1 se 100 tak koi bhi number choose karega.

import random
def guessNumber():
    """Project 2 : Number Guessing Game in Python."""
    number = random.randint(1, 100)
    remaining_guesses = 10
    
#Welcome message
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

#generating loop
    while remaining_guesses > 0:
        print(f"You have {remaining_guesses} guesses left.")

        try:
            guess = int(input("Take a guess of another number. "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
#guessing secret number
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number} correctly in {10 - remaining_guesses + 1} guesses.")
            return
        
        remaining_guesses -= 1
#when all guesses are used
    print(f"\n Sorry, you ran out of guesses. The number I was thinking of was {number}.")
    
    
guessNumber()
#end of the program

        
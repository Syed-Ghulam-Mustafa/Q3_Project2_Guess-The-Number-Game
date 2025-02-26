import random
#generae random number

print("Guess the number between 1 and 100")
number = random.randint(1,100)
attempts = 7  # Initialize attempts counter

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts -= 1  # Decrement attempts
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    elif guess == number:
        print(f"Congratulations! You guessed the number in { 7 -attempts + 1 } attempts.")
        break
    else:
        print("Invalid input!")





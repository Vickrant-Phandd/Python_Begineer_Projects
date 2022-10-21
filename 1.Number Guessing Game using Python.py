# Number Guessing Game using Python

# Import the random module, and display a random number between 1 and 10:

# n 9, guess 5
import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!=guess:
    if guess < n:
        print("Too Low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too High!")
        guess = int(input("Enter number again: "))
    else:
        break
print("Hurry!!!..You guess it right...")

        
    


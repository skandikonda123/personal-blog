import random

number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
print("Congratulations, you guessed the number!")


This is a simple Python program that generates a random number between 1 and 100 and prompts the user to guess the number. 
The program uses a while loop to repeatedly ask the user for their guess until they correctly guess the number.
If the user's guess is too low, the program prints "Too low!" and if it is too high, the program prints "Too high!". 
When the user finally guesses the correct number, the program prints "Congratulations, you guessed the number!".

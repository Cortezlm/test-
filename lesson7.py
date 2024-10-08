# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
# Rule 2: Program must run until the correct number is guessed
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?
import random

def guessing_game():
    number_to_guess = random.randint(1, 20)
    attempts = 0
    max_attempts = 3

    print("Welcome to the guessing game!")
    print("I have selected a number between 1 and 20. You have 3 attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 20:
                print("Please guess a number between 1 and 20.")
                continue

            if guess < number_to_guess:
                print("Higher!")
            elif guess > number_to_guess:
                print("Lower!")
            else:
                print(f"Yes! You guessed it in {attempts} guesses.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

# Start the game
guessing_game()

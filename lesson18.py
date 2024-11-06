# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
# Do not just google the game and copy paste, If you would like to look at a completed version if you get stuck on a step please do so.
#Write your code below this line:
import random

choices = ["rock", "paper", "scissors"]

while True:
    print("\nrock, paper, scissors?")
    player_choice = input("Enter your choice: ").lower()
# Validate player input
    if player_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue
        
        # Generate computer's choice
    computer_choice = random.choice(choices)
        
        # Show both choices
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
        
        # Determine winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "paper" and computer_choice == "rock") or \
        (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
            
        # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing")
        break



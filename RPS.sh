#!/bin/bash

# Function to get the computer's choice
get_computer_choice() {
    local choices=("rock" "paper" "scissors")
    local random_index=$((RANDOM % 3))
    echo "${choices[$random_index]}"
}

# Function to determine the winner
determine_winner() {
    if [ "$1" == "$2" ]; then
        echo "It's a tie!"
    elif [ "$1" == "rock" ] && [ "$2" == "scissors" ]; then
        echo "Rock crushes scissors. You win!"
    elif [ "$1" == "scissors" ] && [ "$2" == "paper" ]; then
        echo "Scissors cuts paper. You win!"
    elif [ "$1" == "paper" ] && [ "$2" == "rock" ]; then
        echo "Paper covers rock. You win!"
    else
        echo "Computer wins!"
    fi
}

# Main game loop
while true; do
    echo "Welcome to Rock-Paper-Scissors!"
    echo "Please choose: rock, paper, or scissors (or type 'exit' to quit):"
    read user_choice

    # Exit condition
    if [ "$user_choice" == "exit" ]; then
        echo "Thanks for playing! Goodbye!"
        break
    fi

    # Validate user choice
    if [[ "$user_choice" != "rock" && "$user_choice" != "paper" && "$user_choice" != "scissors" ]]; then
        echo "Invalid choice. Please choose rock, paper, or scissors."
        continue
    fi

    # Get the computer's choice
    computer_choice=$(get_computer_choice)
    echo "Computer chose: $computer_choice"

    # Determine and display the winner
    determine_winner "$user_choice" "$computer_choice"
done

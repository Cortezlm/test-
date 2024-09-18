#!/bin/bash

# Function to check the number and provide feedback
check_number() {
    local number=$1
    if [[ $number -gt 5 ]]; then
        echo "The number is greater than 5."
    elif [[ $number -lt 5 ]]; then
        echo "The number is less than 5."
    else
        echo "The number is equal to 5."
    fi
}

# Prompt the user for input
read -p "Enter a number between 1 and 10: " user_input

# Check if the input is a valid number between 1 and 10
if [[ $user_input =~ ^[0-9]+$ ]] && (( user_input >= 1 && user_input <= 10 )); then
    # Call the function with the user's input
    check_number $user_input
else
    echo "Invalid input. Please enter a number between 1 and 10."
fi

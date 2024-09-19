#!/bin/bash
# Create a script that ask the user for a number between 1 and 10.  Have the script tell the user if there
# number is greater than 5, less than 5, or equal to 5.  Please use an if/else or elif statement to make this happen.  
# Also put the if/else statemnt inside a function.
# -eq = equal
# -ne = are not equal
# -gt = greater than
# -ge = greater or equal to
# -lt = less than
# -le = less than or equal to
# >= (Greater than or equal to)
# <= (Less than or equalk to)
# > (Greater)
# < (Less)
# == (comparison)
# % (Remainder)
# * (Multiply)
#Here are some helpful commands to make this happen.

# Prompt the user for input
read -p "Enter a number between 1 and 10: " user_input

# Check if the input is a valid number between 1 and 10
if [[ $user_input =~ ^[0-9]+$ ]] && (( user_input >= 1 && user_input <= 10 )); then
    # Call the function with the user's input
    check_number $user_input
else
    echo "Invalid input. Please enter a number between 1 and 10."
fi

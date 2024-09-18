#!/bin/bash
# Bob is back at it again! Now he needs us to script something that if user inserts between 2 to 5, it will print out “Valid Number” and “your number is ___”.
# And if the user input is not between 2 and 5, it will print out “not valid!”
 
#Main
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


#!/bin/bash

# Prompt user for input
read -p "Please enter a number: " number

# Check if the input is between 2 and 5
if [[ "$number" -ge 2 && "$number" -le 5 ]]; then
  echo "Valid Number"
  echo "Your number is $number"
else
  echo "Not valid!"
fi

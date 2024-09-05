#!/bin/bash



while true

do

    read -p "enter a selection: " input



    if [ "$input" -eq 1 ]; then

        echo "Hello World"

    elif [ "$input" -eq 2 ]; then

      ping "google.com"

    elif [ "$input" -eq 3 ]; then

        ifconfig

    else

        echo "Invalid selection. Please try again."

    fi



done




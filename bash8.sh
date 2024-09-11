#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated
# https://linuxize.com/post/bash-case-statement/

read -p "how is your day good or bad" input
case $input in 

    good)
    echo "im haappy your day is good"
    ;;
    bad)
    echo "im sorry to hear that"
    ;;
    *)
    echo "invalid please try again"

;;
esac

x=1
until [ $x = 10 ]
do

    echo "Your number is " $x 
    #((x++))
    x=$((x+1))
done



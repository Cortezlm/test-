# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"
import time

#Start code below this line:
print(time.strftime("%Y-%m-%d %H:%M:%S"))
for i in range(1, 11):
    print(f"{i} Mississippi")
    time.sleep(1)  # Pause for 1 second

# Final message
print("Ready or not, here I come!")
# Write a program in python that splits the bill evenly between group.
# Ask how much they want to tip and how many people


#Example
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("Enter the total bill amount: $"))
tip_percentage = float(input ("Enter the tip percentage"))
people = int(input ("Enter the number of people"))
# Calculate
total_amount = bill *(1 + tip_percentage / 100) 
amount_per_person = total_amount / people

final_amount = "{:.2f}".format(amount_per_person)

print (f"Each person should pay: ${final_amount}")
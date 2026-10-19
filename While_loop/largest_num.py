# Program: Find the largest number entered by the user

# Keep asking the user to enter numbers.

# Requirements:

# Use a while loop.
# Stop when the user enters 0.
# Find the largest number entered.
# Print the largest number at the end.

number = int(input("Enter the num :"))
count = 0
largest = 0

while number != 0:
    if number > largest:
     largest = number
    #count = count + 1
    number = int(input("Enter the num :"))
#print("Total125 entered numbers are :",count)
print("Largest number is :",largest)
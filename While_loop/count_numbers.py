# Count numbers entered by the user

# Write a Python program that keeps asking the user to enter a number.

# Requirements:

# Continue asking for numbers using a while loop.
# Stop when the user enters 0.
# Count how many numbers the user entered.
# At the end, print the total count.

number = int(input("Enter the number :"))

count = 0

while number != 0:
      count = count + 1
      number = int(input("Enter the number :"))
print("The total entered numbers are :",count)
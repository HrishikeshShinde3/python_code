# Keep taking inputs from the user till user 
# enters a 0

# calculate total user

# calculate the total sum 

# calculate the average of all


number = int(input("Enter the number :"))

user = 0 

input_sum = 0

while number != 0:
    input_sum =  input_sum + number
    user = user + 1
    number = int(input("Enter the number :"))
print("Total user are :",user)
print("Total sum is :",input_sum)
print("Average of inputs are :",input_sum/user)


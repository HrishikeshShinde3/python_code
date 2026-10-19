
# atm withdrawal system

# Rules:

# starting balance = 50000
# If amount is greater than the balance → print "Insufficient balance"
# If amount is less than or equal to balance → deduct it and 
# print the remaining balance

# The user should be able to continue withdrawing.
# Stop when the user enters 0.
# At the end, print "Transaction completed".

Available_balance = 50000

Withdrawal_amount = int(input("Enter the amount: "))

while Withdrawal_amount != 0:

    if Withdrawal_amount > Available_balance:
        print("Insufficient balance. Please enter a valid amount.")

    elif Withdrawal_amount >= 1:
        Available_balance = Available_balance - Withdrawal_amount

        print("Withdrawal Successful of amount:", Withdrawal_amount)
        print("Remaining balance is:", Available_balance)

    else:
        print("Invalid amount. Please enter a valid amount!")

    Withdrawal_amount = int(input("Enter the amount: "))

print("Transaction completed")
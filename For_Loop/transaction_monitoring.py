# FROM GIVEN TRANSACTION DATA

#  FIND

# 1 NUMBERR OF TRANSACTIONS
# 2 TOTAL TRANSACTIONS AMOUNT
# 3 NO OF TRANSACTIONS GREATER THAN 10000
# 4 THE HIGHEST TRANSACTION AMOUNT
# 5 PRINT "HIGH VALUE TRANSACTION" FOR 50000 & ABOVE TRANSACTIONS

transactions = [1200, 4500, 800, 15000, 2300, 75000, 3200, 18000, 600]

# 1  NUMBERR OF TRANSACTIONS

no_of_transactions = 0
total_transaction_amout = 0
count= 0

for transaction in transactions:
    no_of_transactions = no_of_transactions + 1
    total_transaction_amout = total_transaction_amout + transaction\


print("Total transactions happened are :",no_of_transactions)
# 2 TOTAL TRANSACTIONS AMOUNT
print("Total transactions amount is :", total_transaction_amout)


# 3 NO OF TRANSACTIONS GREATER THAN 10000
count = 0
for transaction in transactions:
   if transaction > 10000:
         print("This are above 10K transactions :",transaction)

# 4 THE HIGHEST TRANSACTION AMOUNT

print("The highest transaction amount is :",max(transactions))

for transaction in transactions:
    if transaction >= 50000:
        print("This is the high value transaction",transaction)


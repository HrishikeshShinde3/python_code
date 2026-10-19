# 200 & 201 are successful responses 

status_codes = [200, 201, 404, 500, 200, 301, 200, 403, 201, 500]

count = 0

for code in status_codes:
     if code == 200 or code == 201:
        count = count + 1
print("Successful response", count, "times")



#valid transactions

transactions = [1200, -500, 3000, 0, 4500, -200, 1800]

valid_transactions = []

for transaction in transactions:
    if transaction > 0:
        valid_transactions.append(transaction)

print("Valid transactions are:", valid_transactions)



# Find duplicates from list

users = ["Rahul", "Amit", "Sneha", "Rahul", "Priya", "Amit", "Rahul"]

count = {}

for user in users:
    if user in count:
        count[user] += 1
    else:
        count[user] = 1

for user, total in count.items():
    print(user, ":", total)



# Highest salary

salaries = [35000, 42000, 28000, 75000, 51000, 63000]

print("Highest salary is :",max(salaries))
print("Lowest salary is :",min(salaries))


# The user enters the number of products sold repeatedly.

# stock = 100

# Requirements:

# Use a while loop.
# Subtract the sold quantity from the stock.
# Print the remaining stock after each sale.
# Stop when the user enters 0.
# If the user tries to sell more products than available, print "Not enough stock" and do not change the stock.
# At the end, print the final stock.

stock = 100

quantity = int(input("Enter the buying quantity: "))

while quantity != 0:

    if quantity <= stock:
        stock = stock - quantity
        print("Remaining stock is:", stock)
    else:
        print("Not enough stock")

    quantity = int(input("Enter the buying quantity: "))

print("Stock over :", stock)
# find

# Total number of orders
# Total order value
# Number of orders above ₹5,000
# Number of orders below ₹1,000
# Find the second highest order value 
# find below
   # "SMALL ORDER" → below ₹1,000
   # "MEDIUM ORDER" → ₹1,000 to ₹5,000
   # "LARGE ORDER" → above ₹5,000

orders = [1200, 450, 7800, 2500, 15000, 320, 6700, 890, 11200, 4300]

total_orders = 0
total = 0

# Total number of orders

for order in orders:
    total_orders = total_orders + 1
print("All no of orders are :",total_orders)

#Total order value sum

total_order_sum = 0

for order in orders:
    total_order_sum = total_order_sum + order
print("Total orders sum is :", total_order_sum)

# Number of orders above ₹5,000

for order in orders:
    if order > 5000:
        print("Order is greater than 5000. Order amount is :",order)


# Number of orders below ₹1,000

for order in orders:
    if order < 1000:
        print("Order is less than 1000. Order amount is :",order)
        

# Find the second highest order 

orders.sort(reverse=True)
print(orders)
print("Second large order amount is :",orders[1])


# find below
   # "SMALL ORDER" → below ₹1,000
   # "MEDIUM ORDER" → ₹1,000 to ₹5,000
   # "LARGE ORDER" → above ₹5,000


for order in orders:
    if order < 1000:
        print("Order is Small :", order)
    elif 1000 < order < 5000:
        print("Order is Medium :", order)
    else:
        print("Order is Large :", order)


        






    




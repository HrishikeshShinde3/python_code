
# Add delivery charges of 65 rs for below 500rs orders

orders = [45,65,766,555,25,75,65]

for order in orders:
    if order < 500:
        delivery_charges = order + 65
        print("Delivery charges applied : ", delivery_charges)
    else:
        print("Delivery charges Not applied : ", order)